import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple


def slugify(text: str, max_len: int = 60) -> str:
    """Converts a title into a filesystem-safe kebab-case slug."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text).strip("-")
    return text[:max_len].rstrip("-") or "article"


def load_seen_state(state_file: str = "state/seen_entries.json") -> Set[str]:
    """Loads previously processed article URL hashes to prevent duplicate file generation."""
    path = Path(state_file)
    if not path.exists():
        return set()
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return set(data.get("seen_hashes", []))
    except Exception:
        return set()


def save_seen_state(seen_hashes: Set[str], state_file: str = "state/seen_entries.json") -> None:
    """Persists seen URL hashes to disk."""
    path = Path(state_file)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            {
                "last_updated": datetime.now(timezone.utc).isoformat(),
                "seen_hashes": sorted(list(seen_hashes)),
            },
            f,
            indent=2,
        )


def compute_url_hash(url: str) -> str:
    """Computes a SHA-256 hash of a normalized URL."""
    clean_url = url.split("?")[0].strip().lower()
    return hashlib.sha256(clean_url.encode("utf-8")).hexdigest()


def write_article_file(
    item: Dict[str, Any], 
    day_dir: Path, 
    index_num: int
) -> Tuple[Path, str]:
    """Writes an individual markdown file for a single article."""
    title = item.get("title", "Untitled Article")
    slug = slugify(title)
    filename = f"{index_num:02d}-{slug}.md"
    file_path = day_dir / filename

    tags_formatted = ", ".join([f"`{t}`" for t in item.get("tags", [])])
    author = item.get("author") or item.get("source") or "Unknown"
    pub_date = item.get("published_date", "N/A")
    url = item.get("url", "")
    source = item.get("source", "")
    summary = item.get("summary", "").strip() or "No summary provided."

    md_content = f"""# {title}

- **URL:** {url}
- **Author:** {author}
- **Published Date:** {pub_date}
- **Tags:** {tags_formatted}
- **Source:** {source}

---

## Summary
{summary}
"""

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    return file_path, filename


def save_daily_digest(
    items: List[Dict[str, Any]], 
    report_root: str = "report",
    state_file: str = "state/seen_entries.json"
) -> Tuple[str, int]:
    """
    Creates day-wise folder under report/YYYY-MM-DD/ and writes individual
    markdown files for each new article. Also generates a day-level README.md.
    """
    if not items:
        return "", 0

    seen_hashes = load_seen_state(state_file)
    now = datetime.now(timezone.utc)
    day_str = now.strftime("%Y-%m-%d")
    day_dir = Path(report_root) / day_str
    day_dir.mkdir(parents=True, exist_ok=True)

    saved_entries: List[Dict[str, Any]] = []
    current_index = len(list(day_dir.glob("[0-9]*.md"))) + 1

    for item in items:
        url_hash = compute_url_hash(item.get("url", ""))
        if url_hash in seen_hashes:
            continue

        file_path, filename = write_article_file(item, day_dir, current_index)
        seen_hashes.add(url_hash)
        current_index += 1

        saved_entries.append({
            "title": item["title"],
            "url": item["url"],
            "filename": filename,
            "author": item.get("author", "Unknown"),
            "source": item.get("source", ""),
            "tags": item.get("tags", []),
            "published_date": item.get("published_date", "Recent")
        })

    # Save state
    save_seen_state(seen_hashes, state_file)

    if not saved_entries:
        print(f"No new unseen articles to save for {day_str}.")
        return str(day_dir), 0

    # Create/update day-wise README.md summarizing all articles of the day
    day_readme = day_dir / "README.md"
    readme_lines = [
        f"# Daily Digest: {day_str}\n",
        f"> Curated technical digest for Distributed Systems & Databases. Aggregated **{len(saved_entries)}** new articles on {now.strftime('%A, %B %d, %Y')}.\n",
        "| # | Article | Source / Author | Tags |",
        "| :---: | :--- | :--- | :--- |",
    ]

    for idx, entry in enumerate(saved_entries, start=1):
        safe_title = entry["title"].replace("|", "-")
        tags_str = ", ".join([f"`{t}`" for t in entry["tags"][:3]])
        readme_lines.append(
            f"| {idx} | [{safe_title}]({entry['filename']}) ([Source]({entry['url']})) | {entry['source']} | {tags_str} |"
        )

    with open(day_readme, "w", encoding="utf-8") as f:
        f.write("\n".join(readme_lines) + "\n")

    print(f"Saved {len(saved_entries)} article files into {day_dir}")
    return str(day_dir), len(saved_entries)


def update_root_index(report_root: str = "report", output_index: str = "INDEX.md") -> None:
    """Scans all day-wise folders in report/ and regenerates the root INDEX.md catalog."""
    base_dir = Path(report_root)
    if not base_dir.exists():
        return

    # Find all day directories matching YYYY-MM-DD
    day_dirs = sorted([d for d in base_dir.iterdir() if d.is_dir() and re.match(r"^\d{4}-\d{2}-\d{2}$", d.name)], reverse=True)
    if not day_dirs:
        return

    catalog: List[Dict[str, Any]] = []

    for d in day_dirs:
        day_str = d.name
        articles = list(d.glob("[0-9]*.md"))
        article_count = len(articles)

        # Collect sample tags
        tags: Set[str] = set()
        for art in articles[:5]:
            try:
                with open(art, "r", encoding="utf-8") as f:
                    content = f.read(500)
                    match = re.search(r"\*\*Tags:\*\*\s*(.+)", content)
                    if match:
                        found_tags = re.findall(r"`([^`]+)`", match.group(1))
                        tags.update(found_tags)
            except Exception:
                pass

        sample_tags_str = ", ".join([f"`{t}`" for t in sorted(list(tags))[:4]])
        catalog.append({
            "date": day_str,
            "dir_path": f"{report_root}/{day_str}",
            "count": article_count,
            "tags": sample_tags_str or "Systems & Databases"
        })

    lines = [
        "# 🗜️ Compactor Digest Archive\n",
        "> Automated daily technical intelligence in Distributed Systems, Databases, Storage Engines, and Infrastructure.\n",
        f"**Total Editions:** {len(catalog)}\n",
        "| Date | Digest Link | Total Articles | Key Topics |",
        "| :--- | :--- | :---: | :--- |"
    ]

    for entry in catalog:
        lines.append(
            f"| {entry['date']} | [Browse Day's Articles]({entry['dir_path']}/README.md) | {entry['count']} | {entry['tags']} |"
        )

    with open(output_index, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Updated {output_index} with {len(catalog)} daily editions.")
