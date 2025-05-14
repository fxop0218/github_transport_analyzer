# GitHub Transport Repository Analyzer 🚗

This CLI tool helps you search and analyze GitHub repositories related to transportation, mobility, ride-sharing, or similar domains. It uses the GitHub public API and implements caching and dynamic search strategies to reduce API usage.

---

## 📦 Features

- 🔍 Search for repositories by keyword or by organization
- 🔄 Filter by programming language
- 📊 Sort results by stars or creation date
- 💡 Strategy Pattern for flexible query construction
- 🧠 Smart caching with expiration using `shelve`
- 🖥️ Clean CLI built with [Typer](https://typer.tiangolo.com/) and [Rich](https://rich.readthedocs.io/)

---

## 🚀 Installation

```bash
git clone https://github.com/fxop0218/github_transport_analyzer.git
cd github_transport_analyzer
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🧪 Usage

Launch the CLI with:

```bash
python run.py [OPTIONS] TERM
```

---

## 🔍 Search Modes (Strategy Pattern)

The CLI supports **two modes** of search using the `--mode` (or `-m`) option. The default is `term`.

### 1. Term-Based Search *(default)*
- **Purpose**: Search by general keywords like `taxi`, `mobility`, etc.
- **Mode**: `term`


```bash
python run.py taxi -l python -s stars -n 5
```
windows:
```bash
python.py run.py taxi -l python -s stars -n 5
```

This will:
- Search for repositories containing the word `taxi`
- Filter by Python language
- Sort by most starred
- Limit to top 5 results

### 2. Organization-Based Search
- **Purpose**: Search all public repositories inside a specific GitHub organization
- **Mode**: `org`

```bash
python run.py openai -m org -n 3
```

```bash
python.py run.py openai -m org -n 3
```

This will:
- Search for public repositories belonging to the `openai` organization
- Limit to top 3

You can combine `--language`, `--sort`, and `--limit` options here as well.

---

## 💾 Caching

To avoid hitting the GitHub API rate limits, the app stores responses in a disk-based cache using Python’s `shelve` module. Cached results expire automatically after **1 hour**.

---

## 🧪 Testing

Run all tests using `pytest`:

```bash
pytest -v
```

---

## 🛠 Project Structure

```
github_transport_analyzer/
├── app/
│   ├── main.py               # CLI logic with Typer and Rich
│   ├── github_client.py     # GitHub API client using Strategy pattern
│   ├── cache.py             # Persistent TTL cache
│   └── strategies/          # Search strategies and factory
├── tests/                   # Pytest unit tests
├── run.py                   # Entry point script to launch CLI
├── README.md
└── requirements.txt
```

---

## 📎 License

MIT License
