from google_play_scraper import Sort, reviews
import pandas as pd
import os
os.makedirs("../data", exist_ok=True)


def scrape_reviews(app_id, bank_name, max_reviews=500):
    result, _ = reviews(
        app_id,
        lang='en',
        country='us',
        sort=Sort.NEWEST,
        count=max_reviews,
    )

    if not result:
        print(f"No reviews found for {bank_name}")
        return pd.DataFrame()

    print(f"Available keys for {bank_name}:", result[0].keys())  # 🔍 Inspect once

    df = pd.DataFrame(result)

    # Use correct column names based on actual keys (adjust if different)
    if all(key in df.columns for key in ['content', 'score', 'at']):
        df = df[['content', 'score', 'at']]
        df.rename(columns={'content': 'review', 'score': 'rating', 'at': 'date'}, inplace=True)
        df['bank'] = bank_name
        df['source'] = 'Google Play'
        return df
    else:
        print(f"Unexpected structure for {bank_name}. Please review keys.")
        return pd.DataFrame()

# Run for all 3 banks
cbe_df = scrape_reviews('com.combanketh.mobilebanking', 'CBE')
boa_df = scrape_reviews('com.boa.boaMobileBanking', 'Bank of Abyssinia')
dashen_df = scrape_reviews('com.dashen.dashensuperapp', 'Dashen Bank')

# Combine and save
combined_df = pd.concat([cbe_df, boa_df, dashen_df], ignore_index=True)
combined_df.to_csv('../data/fintech_reviews.csv', index=True)

print("✅ All reviews scraped and saved to /data.")
