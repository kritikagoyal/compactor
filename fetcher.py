import html
import re
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional
from dateutil import parser as date_parser
import feedparser


def clean_text(raw_text: str) -> str:
    """Strips HTML tags, arXiv LaTeX artifacts, and normalizes whitespace."""
    if not raw_text:
        return ""

    # 1. Unescape HTML entities (e.g. &amp; -> &, &lt; -> <)
    text = html.unescape(raw_text)

    # 2. Strip HTML tags
    text = re.sub(r"<[^>]+>", " ", text)

    # 3. Strip arXiv LaTeX artifacts ($...$, \command{...})
    text = re.sub(r"\$\$.*?\$\$", "", text)
    text = re.sub(r"\$.*?\$", "", text)
    text = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", text)
    text = re.sub(r"\\[a-zA-Z]+", "", text)

    # 4. Collapse extra whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_author(entry: Any, fallback_source: str) -> str:
    """Extracts author name from feed entry with fallback."""
    if hasattr(entry, "author") and entry.author:
        return clean_text(entry.author)

    if hasattr(entry, "author_detail") and getattr(entry.author_detail, "name", None):
        return clean_text(entry.author_detail.name)

    if hasattr(entry, "authors") and entry.authors:
        names = [a.get("name") for a in entry.authors if isinstance(a, dict) and a.get("name")]
        if names:
            return ", ".join(names[:3])

    if hasattr(entry, "dc_creator") and entry.dc_creator:
        return clean_text(entry.dc_creator)

    return fallback_source


def parse_published_date(entry: Any) -> Optional[datetime]:
    """Safely extracts and normalizes publication date to UTC datetime."""
    for field in ("published", "pubDate", "updated", "created"):
        val = getattr(entry, field, None) or (entry.get(field) if isinstance(entry, dict) else None)
        if val:
            try:
                dt = date_parser.parse(val)
                if dt.tzinfo is None:
                    return dt.replace(tzinfo=timezone.utc)
                return dt.astimezone(timezone.utc)
            except Exception:
                continue

    # Fallback to parsed time structs if available
    for struct_field in ("published_parsed", "updated_parsed"):
        t_struct = getattr(entry, struct_field, None)
        if t_struct:
            try:
                return datetime(*t_struct[:6], tzinfo=timezone.utc)
            except Exception:
                continue

    return None


def fetch_feed(source: Dict[str, Any], lookback_hours: int = 36) -> List[Dict[str, Any]]:
    """Fetches an RSS/Atom feed and extracts standardized article metadata."""
    source_name = source.get("name", "Unknown Source")
    url = source.get("url")
    default_tags = source.get("default_tags", [])

    if not url:
        return []

    cutoff = datetime.now(timezone.utc) - timedelta(hours=lookback_hours)
    parsed = feedparser.parse(url)
    items: List[Dict[str, Any]] = []

    for entry in parsed.entries:
        pub_dt = parse_published_date(entry)

        # Enforce lookback window if date is available
        if pub_dt and pub_dt < cutoff:
            continue

        raw_title = entry.get("title", "")
        raw_summary = entry.get("summary", "") or entry.get("description", "")
        link = entry.get("link", "").strip()

        title = clean_text(raw_title)
        summary = clean_text(raw_summary)
        author = extract_author(entry, source_name)

        if not title or not link:
            continue

        # Format publication date nicely
        formatted_date = pub_dt.strftime("%Y-%m-%d %H:%M UTC") if pub_dt else "Recent"

        items.append({
            "title": title,
            "url": link,
            "author": author,
            "published_date": formatted_date,
            "published_dt": pub_dt or datetime.now(timezone.utc),
            "summary": summary,
            "source": source_name,
            "default_tags": list(default_tags),
        })

    return items
