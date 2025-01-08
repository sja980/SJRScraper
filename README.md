# SJRScraper

SJRScraper is a Python-based web scraper built using the [Scrapy](https://scrapy.org/) web scraping and crawling framework. It is designed to extract specific information from the [SCImago Journal & Country Rank (SJR)](https://www.scimagojr.com/) website, including links to journal homepages, submission guidelines, and contact emails. Other journal data is readily accessible from the SJR website and can be exported in the form of a .csv file.

## Features

- Scrapes journal homepage URLs
- Retrieves "How to publish in this journal" links
- Extracts contact email addresses

## Installation

# Clone the repository and navigate to the project directory
git clone https://github.com/sja980/SJRScraper.git
cd SJRScraper

# Create a virtual environment (optional)
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install the required dependencies
pip install -r requirements.txt

## To Use
# Ensure you are in the project directory and the virtual environment is activated
# Run the scraper
python SJR_Scraper.py

# The scraped data will be saved to journalprofilelinks2024.txt

##License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Thanks to SSCImago, (n.d.). SJR — SCImago Journal & Country Rank [Portal] for providing the data.
