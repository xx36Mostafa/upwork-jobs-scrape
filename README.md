# Job Scraper for Upwork

This Python script scrapes job listings from Upwork based on a specific topic and stores the data in an SQLite database. It extracts details such as job titles, prices, descriptions, and posting dates to help users analyze job opportunities programmatically.

## Features

- Scrapes job postings from Upwork using a provided keyword.
- Stores job details (title, price, description, date, and link) in an SQLite database.
- Ensures no duplicate entries by checking existing links in the database.
- Provides a flexible structure for scraping multiple pages.

## Prerequisites

- Python 3.8 or higher.
- Required packages:
  - `tls_client`
  - `BeautifulSoup` from `bs4`
  - `sqlite3` (built-in Python module)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/job-scraper.git
   cd job-scraper
   ```
2. Install the required Python packages:
```bash
  pip install tls_client beautifulsoup4
  ```
