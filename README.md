#  Fintech App Review Analytics – Tenx Week 2 Challenge

Analyze customer feedback on Ethiopian mobile banking apps to help improve app performance and user satisfaction.  
This project simulates real-world consulting work by scraping, cleaning, and analyzing Google Play Store reviews using Python and NLP.

---

##  Challenge Overview

Omega Consultancy is supporting three banks in Ethiopia:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

 task is to:
- Collect Google Play Store reviews
- Clean and preprocess the data
- Perform sentiment and thematic analysis using NLP
- (Pending) Store the results in Oracle DB
- (Pending) Visualize findings and provide recommendations

---

##  Completed Tasks

### Task 1: Data Collection & Preprocessing

- ✅ Scraped 400+ reviews per bank using `google-play-scraper`
- ✅ Removed duplicates and missing values
- ✅ Normalized dates to `YYYY-MM-DD`
- ✅ Saved as `data/clean_reviews.csv`

### Task 2: Sentiment & Thematic Analysis

- ✅ Applied `distilbert-base-uncased-finetuned-sst-2-english` for sentiment labeling
- ✅ Extracted keywords using TF-IDF
- ✅ Grouped keywords into manual themes (e.g., "login issue", "app crash")
- ✅ Output saved as `data/final_reviews.csv`

---

##  Setup Instructions

###  Create Virtual Environment

```bash
python -m venv .venv
source .venv/Scripts/activate    # Windows

