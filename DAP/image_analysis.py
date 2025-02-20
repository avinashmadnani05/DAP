import pandas as pd
import requests
import os
# Load data
df = pd.read_csv("reddit_memes.csv")

# Create directory for images
os.makedirs("meme_images", exist_ok=True)
# Download images
for index, row in df.iterrows():
    image_url = row["url"]
    file_name = f"meme_images/{index}.jpg"

    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            with open(file_name, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Downloaded: {file_name}")
        else:
            print(f"Failed: {image_url}")
    except Exception as e:
        print(f"Error: {e}")



# from nltk.tokenize import word_tokenize
# from collections import Counter

# words = word_tokenize(" ".join(df["title"]))
# word_counts = Counter(words)

# print(word_counts.most_common(10))  # Most common words

