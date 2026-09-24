import argparse
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict
import yaml

from fetcher import fetch_feed
from tagger import process_and_tag
from archiver import save_daily_digest, update_root_index


def load_config(config_path: str = "config/feeds.yaml") -> Dict[str, Any]:
    """Loads configuration and taxonomy mappings."""
    path = Path(config_path)
    if not path.exists():
        print(f"Error: Config file not found at {config_path}")
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def git_auto_commit(report_dir: str = "report", index_file: str = "INDEX.md", state_dir: str = "state") -> None:
    """Stages generated reports and state files and creates a git commit."""
    try:
        now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        # Check if there are changes to commit
        status_proc = subprocess.run(["git", "status", "--porcelain", report_dir, index_file, state_dir], capture_output=True, text=True)
        if not status_proc.stdout.strip():
            print("Git: No changes detected to commit.")
            return

        print("Git: Staging report and index files...")
        subprocess.run(["git", "add", report_dir, index_file, state_dir], check=True)
        commit_msg = f"chore(digest): daily digest for {now_str}"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        print(f"Git: Committed changes: '{commit_msg}'")
    except Exception as e:
        print(f"Git auto-commit skipped or failed: {e}")


def main():
    parser = argparse.ArgumentParser(description="Compactor: Distributed Systems & Databases Daily Digest Engine")
    parser.add_argument("--config", default="config/feeds.yaml", help="Path to feeds configuration YAML")
    parser.add_argument("--report-dir", default="report", help="Root directory for day-wise reports")
    parser.add_argument("--hours", type=int, default=None, help="Lookback window in hours (overrides config)")
    parser.add_argument("--auto-commit", action="store_true", help="Automatically commit report and index changes to git")

    args = parser.parse_args()

    config = load_config(args.config)
    settings = config.get("settings", {})
    sources = config.get("sources", [])
    taxonomy = config.get("taxonomy", {})

    lookback_hours = args.hours or settings.get("lookback_hours", 36)

    print(f"=== Compactor Daily Digest Engine ===")
    print(f"Sources: {len(sources)} | Lookback: {lookback_hours} hours | Target: {args.report_dir}/")

    all_raw_items = []
    for src in sources:
        try:
            items = fetch_feed(src, lookback_hours=lookback_hours)
            all_raw_items.extend(items)
            print(f"  ✓ {src['name']}: {len(items)} items")
        except Exception as e:
            print(f"  ✗ {src.get('name', 'Unknown')}: {e}")

    print(f"\nTotal raw articles collected: {len(all_raw_items)}")

    # 1. Deduplicate & enrich with taxonomy tags
    tagged_items = process_and_tag(all_raw_items, taxonomy)
    print(f"Unique categorized articles: {len(tagged_items)}")

    # 2. Save individual markdown files under report/YYYY-MM-DD/
    day_dir, saved_count = save_daily_digest(tagged_items, report_root=args.report_dir)

    # 3. Rebuild root INDEX.md catalog
    update_root_index(report_root=args.report_dir, output_index="INDEX.md")

    # 4. Optional Git auto-commit
    if args.auto_commit:
        git_auto_commit(report_dir=args.report_dir)

    print("\nDigest pipeline finished successfully.")


if __name__ == "__main__":
    main()
