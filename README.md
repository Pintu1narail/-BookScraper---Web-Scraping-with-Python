# -BookScraper---Web-Scraping-with-Python
"A Python web scraper built with BeautifulSoup and Requests to extract book details (title, price, rating, availability) from toscrape.com with full pagination support."

📚 BookScraper: Automated Book Data Extractor
A Python-based web scraper that automatically extracts book information from ://toscrape.com. It navigates through all pagination levels and saves the data into a structured CSV format.
🚀 Features
Full Pagination Support: Automatically crawls through all pages of the website.
Data Extracted: Captures Book Title, Price, Stock Status, and Star Ratings.
Rating Conversion: Converts text-based ratings (e.g., "Three") into numerical values (e.g., 3) for easier data analysis.
Custom Headers: Uses realistic User-Agents to prevent being blocked by the server.
CSV Export: Saves all extracted data into a book_scrape.csv file.
🛠️ Tech Stack
Python 3.x
Requests: For handling HTTP requests.
BeautifulSoup4: For parsing HTML content.
CSV Module: For data storage.
📋 How to Run
Clone the repository:
bash
git clone https://github.com
Use code with caution.
Install dependencies:
bash
pip install requests beautifulsoup4
Use code with caution.
Run the script:
bash
python scraper.py
Use code with caution.
📊 Sample Output (CSV Structure)
Title	Price	Stock_status	Rating
A Light in the Attic	51.77	In stock	3
Tipping the Velvet	53.74	In stock	1
