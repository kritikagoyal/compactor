# 🗜️ Compactor

> **Automated daily intelligence digest for engineers working in Distributed Systems, Storage Engines, and Databases.**

`Compactor` aggregates, deduplicates, tags, and archives high-signal technical articles, engineering blogs, and research preprints (arXiv cs.DC / cs.DB) into a day-wise markdown directory structure.

---

## 📂 Repository Structure

```text
compactor/
├── .github/
│   └── workflows/
│       └── digest.yml       # Daily GitHub Actions cron automation
├── config/
│   └── feeds.yaml           # Source definitions & keyword taxonomy
├── report/                  # Daily archive root
│   └── YYYY-MM-DD/          # Day-wise folder
│       ├── README.md        # Day's digest table of contents
│       ├── 01-article-a.md  # Individual article markdown file
│       └── 02-article-b.md  # Individual article markdown file
├── state/
│   └── seen_entries.json    # Deduplication state (URL SHA-256 hashes)
├── fetcher.py               # Feed ingestion & text normalization
├── tagger.py                # Taxonomy matching & article tagging
├── archiver.py              # Day-wise report & index generation
├── main.py                  # CLI pipeline runner
├── INDEX.md                 # Master historical catalog of all digests
└── requirements.txt         # Dependencies (feedparser, pyyaml, python-dateutil)
```

---

## 📑 Article Markdown Format

Every discovered article is saved as an individual `.md` file inside its day's folder (`report/YYYY-MM-DD/`):

```markdown
# Optimizing LSM Write Amplification on ZNS SSDs

- **URL:** https://example.com/blog/lsm-zns
- **Author:** Jane Doe
- **Published Date:** 2026-09-24 04:15 UTC
- **Tags:** `databases`, `kv-store`, `storage-engine`
- **Source:** CockroachDB Engineering

---

## Summary
A technical breakdown of how zoned namespaces (ZNS) mitigate write amplification factor (WAF)...
```

---

## 🏷️ Covered Tags & Taxonomy

Articles are automatically classified against a domain-specific systems taxonomy defined in [`config/feeds.yaml`](config/feeds.yaml):

- **Distributed Systems:** Consensus, Raft, Paxos, 2PC, vector clocks, CAP, sharding, replication.
- **Databases:** Storage engines, LSM-trees, B-trees, WAL, MVCC, query planning, ACID.
- **Specific DBs & KV Stores:** Redis/Valkey, Cassandra/ScyllaDB, PostgreSQL, MySQL, CockroachDB, TiDB, RocksDB, Pebble.
- **Streaming & Messaging:** Kafka, Confluent, Redpanda, Pulsar.
- **Coordination & Cloud Runtime:** ZooKeeper, etcd, Docker, Kubernetes, containerd.
- **Academic Research:** arXiv cs.DC (Distributed Computing), arXiv cs.DB (Databases).

---

## ⚙️ Automated Execution (GitHub Actions)

A GitHub Actions workflow ([`.github/workflows/digest.yml`](.github/workflows/digest.yml)) runs every day at **06:00 UTC**:
1. Checks out the repository.
2. Installs Python dependencies.
3. Fetches new articles within the lookback window.
4. Generates new `.md` files in `report/YYYY-MM-DD/`.
5. Updates `INDEX.md` and commits the new files directly to the repository.

You can also trigger it on-demand via the **Actions** tab using the `Run workflow` button (`workflow_dispatch`).

---

## 🚀 Running Locally

```bash
# 1. Clone repository
git clone git@github.com:kritikagoyal/compactor.git
cd compactor

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Run pipeline
python main.py

# Optional: Run with custom lookback hours and auto-commit
python main.py --hours 48 --auto-commit
```
