# SVU Cast Analysis

This repo contains code to scrape and analyze *Law & Order: SVU* IMDb data.
- **svu_analysis.ipynb**: A Jupyter Notebook with code to analyze cast appearances in each episode
- **svu_cleaning.ipynb**: A Jupyter Notebook with code to clean the data from web scraping and create a dictionary with actor, roles, and episodes in which they appeared
- cast.csv and episode.csv: Cast and episode data scraped from IMDb


In the scrapy folder:
- **svu_scrapy.py**: Python script which is a Scrapy spider used to scrape episode and cast data for each episode from IMDb
  - Other Scrapy files: items.py, middlewares.py, pipelines.py, settings.py
