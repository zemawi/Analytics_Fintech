import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("sentiment_reviews.csv")

# Extract top keywords
vectorizer = TfidfVectorizer(max_df=0.9, stop_words="english", max_features=100)
X = vectorizer.fit_transform(df["review"])
keywords = vectorizer.get_feature_names_out()

# Save top 30 keywords
top_keywords = pd.DataFrame(keywords, columns=["keyword"])
top_keywords.to_csv("keywords.csv", index=False)
print(" Keywords saved to keywords.csv")
df["theme"] = df["review"].apply(lambda r: "Account Access" if "login" in r else
                                                "Performance" if "slow" in r else
                                                "App Stability" if "crash" in r else
                                                "Other")

df.to_csv("final_reviews.csv", index=False)
print(" Final reviews with themes saved to final_reviews.csv")
