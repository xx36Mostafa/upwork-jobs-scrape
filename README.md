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
3. Ensure `sqlite3` is enabled in your Python environment (it is included by default).
## Usage

1. Open the script (`main.py`) and modify the `topic` variable to your desired keyword. The default is set to `'data scraping'`.

2. Run the script:
   ```bash
   python main.py
   ```
3. The script will:
Scrape job postings related to the topic.
Insert unique job details into an SQLite database (jobs.db).

## Database Schema

The script creates an SQLite database (`jobs.db`) with a table named articles. The schema is as follows:

`id`: Integer, primary key.
`date`: Text, date of job posting.
`tittle`: Text, job title.
`price`: Text, job price.
`description`: Text, job description.
`link`: Text, link to the job posting.

