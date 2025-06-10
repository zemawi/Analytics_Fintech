import pandas as pd
from transformers import pipeline

# Load sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Load cleaned reviews
df = pd.read_csv("clean_reviews.csv")

# Analyze sentiments (this takes time!)
results = sentiment_pipeline(df["review"].tolist(), truncation=True)

# Add results to DataFrame
df["sentiment_label"] = [r["label"] for r in results]
df["sentiment_score"] = [r["score"] for r in results]

# Save to new file
df.to_csv("sentiment_reviews.csv", index=False)
print(" Sentiment analysis complete and saved to sentiment_reviews.csv")
