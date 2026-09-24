import re
from typing import Any, Dict, List, Set


def tag_article(item: Dict[str, Any], taxonomy: Dict[str, Any]) -> List[str]:
    """Matches article title and summary against taxonomy keywords and combines with default tags."""
    content = f"{item.get('title', '')} {item.get('summary', '')}".lower()
    assigned_tags: Set[str] = set(item.get("default_tags", []))

    for tag_name, tag_def in taxonomy.items():
        keywords = tag_def.get("keywords", [])
        for kw in keywords:
            # Word boundary matching for short terms (e.g. sql, zk, k8s, wal), substring for multi-word
            kw_clean = kw.lower().strip()
            if len(kw_clean) <= 4:
                pattern = rf"\b{re.escape(kw_clean)}\b"
                if re.search(pattern, content):
                    assigned_tags.add(tag_name)
                    break
            else:
                if kw_clean in content:
                    assigned_tags.add(tag_name)
                    break

    # If no specific tags matched, ensure at least high-level category tag exists if available
    if not assigned_tags:
        assigned_tags.add("distributed-systems")

    return sorted(list(assigned_tags))


def process_and_tag(
    items: List[Dict[str, Any]], 
    taxonomy: Dict[str, Any]
) -> List[Dict[str, Any]]:
    """Deduplicates items and enriches each with matched tags."""
    seen_urls: Set[str] = set()
    processed: List[Dict[str, Any]] = []

    for item in items:
        url = item.get("url", "").strip()
        if not url or url in seen_urls:
            continue
        seen_urls.add(url)

        item_copy = dict(item)
        item_copy["tags"] = tag_article(item, taxonomy)
        processed.append(item_copy)

    # Sort descending by published date
    processed.sort(key=lambda x: x.get("published_dt"), reverse=True)
    return processed
