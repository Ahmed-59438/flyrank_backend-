# Web Scraping & Data Extraction Pipeline

A modular, production-ready Python web scraping pipeline built according to **Clean Architecture** and **Single Responsibility Principles (SRP)**.

> 📖 **New to Python, Scraping, or Clean Architecture?**
> We have created a comprehensive, easy-to-read [Beginner's Guide to Concepts](file:///c:/Users/mahma/backend/flyrank_task_3/web_scraper/beginner_guide.md) that explains every single tool and concept used in this repository in simple words!

This pipeline scrapes book information from [books.toscrape.com](https://books.toscrape.com/), cleans and validates the extracted records, and exports them to structured **JSON** and **CSV** files.

---

## 🎯 Architecture & Data Flow

```
Website (books.toscrape.com)
   │
   ▼
[1. scraper.py] ──► Downloads raw HTML (Resilience, Retry & Rate Limiting)
   │
   ▼
[2. parser.py]  ──► Parses DOM Tree with BeautifulSoup & lxml
   │
   ▼
[3. cleaner.py] ──► Sanitizes strings & converts prices to numeric float
   │
   ▼
[4. validator.py] ──► Validates records against quality schema rules
   │
   ▼
[5. saver.py]    ──► Exports datasets to JSON and CSV formats
```

---

## 📁 Project Structure

```
flyrank_task_3/web_scraper/
│
├── data/
│   ├── books.json          # Output JSON dataset
│   └── books.csv           # Output CSV dataset
│
├── config.py               # Centralized configuration parameters
├── logger.py               # Dual-target (console + file) logging setup
├── scraper.py              # HTTP fetcher with retry & backoff logic
├── parser.py               # DOM parsing & HTML extraction module
├── cleaner.py              # String normalization & price conversion module
├── validator.py            # Quality control & schema validation module
├── saver.py                # JSON & CSV file exporter module
├── main.py                 # Pipeline controller & orchestrator
│
├── beginner_guide.md       # Complete beginner-friendly concepts guide
├── requirements.txt        # Third-party dependencies
└── README.md               # Project documentation
```

---

## 🛠️ Installation & Requirements

### Prerequisites
- Python 3.10+
- `pip`

### Step 1: Navigate to Project Directory
```bash
cd flyrank_task_3/web_scraper
```

### Step 2: Create Virtual Environment
```bash
python -m venv .venv
```
Activate on Windows:
```cmd
.venv\Scripts\activate
```
Activate on Linux/macOS:
```bash
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Execution

Run the main pipeline controller:
```bash
python main.py
```

### Log Output Example:
```text
2026-07-21 07:05:00 | INFO    | main | Starting Web Scraping & Data Extraction Pipeline
2026-07-21 07:05:01 | INFO    | scraper | Fetching URL: https://books.toscrape.com/catalogue/page-1.html (Attempt 1/3)
2026-07-21 07:05:02 | INFO    | scraper | Successfully fetched page-1.html [Status: 200]
2026-07-21 07:05:02 | INFO    | parser | Successfully extracted 20 books from page HTML.
2026-07-21 07:05:02 | INFO    | cleaner | Cleaned 20 book records.
2026-07-21 07:05:02 | INFO    | validator | Validation complete. Valid records: 20, Skipped invalid: 0
2026-07-21 07:05:02 | INFO    | saver | Successfully saved 20 records to JSON: data/books.json
2026-07-21 07:05:02 | INFO    | saver | Successfully saved 20 records to CSV: data/books.csv
```

---

## 💾 Output Formats

### JSON (`data/books.json`)
```json
[
    {
        "title": "A Light in the Attic",
        "price": 51.77,
        "availability": "In stock",
        "rating": "Three"
    }
]
```

### CSV (`data/books.csv`)
```csv
title,price,availability,rating
"A Light in the Attic",51.77,"In stock","Three"
```

---

## 🔮 Future Improvements

1. **Asynchronous Scraping**: Integrate `httpx` or `aiohttp` with `asyncio` for multi-concurrent page fetching.
2. **Proxy Rotation**: Add IP rotation to bypass IP-based rate limits on large-scale web crawling.
3. **Database Persistence**: Integrate PostgreSQL via `SQLAlchemy` or `Tortoise-ORM` for direct database ingestion.
4. **`robots.txt` Compliance Parser**: Programmatically parse site `robots.txt` before scraping.
