from google_play_scraper import reviews
import pandas as pd
from datetime import datetime

# Define app IDs and friendly bank names
banks = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []

# Loop through each bank
for bank_name, app_id in banks.items():
    print(f"Scraping reviews for {bank_name}...")
    
    result, _ = reviews(
        app_id,
        lang='en',
        country='us',
        count=400,
        filter_score_with=None  # Gets all reviews regardless of score
    )

    for r in result:
        review_text = r.get('content')
        rating = r.get('score')
        date = r.get('at')

        if review_text and rating and date:
            all_reviews.append({
                "review": review_text.strip(),
                "rating": rating,
                "date": date.strftime('%Y-%m-%d'),
                "bank": bank_name,
                "source": "Google Play"
            })

# Create DataFrame
df = pd.DataFrame(all_reviews)

# Drop duplicates
df.drop_duplicates(subset=["review", "rating", "date", "bank"], inplace=True)

# Drop missing data
df.dropna(inplace=True)

# Reset index
df.reset_index(drop=True, inplace=True)

# Save to CSV
df.to_csv("clean_reviews.csv", index=False)

print(f"✅ Done! Saved {len(df)} cleaned reviews to clean_reviews.csv")
