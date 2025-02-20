import praw
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Reddit API Credentials (From .env file)
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
    redirect_uri=os.getenv("REDDIT_REDIRECT_URI")  # Not actively used for scripts
)

# Subreddits to scrape
subreddits = ["memes", "dankmemes", "wholesomememes"]

# Data storage
meme_data = []

# Fetch posts
for sub in subreddits:
    subreddit = reddit.subreddit(sub)
    
    for post in subreddit.hot(limit=10000):  # Fetch top 100 posts
        # Default URL
        image_url = post.url

        # Check if the URL is a direct image link (jpg, png, gif)
        if not image_url.endswith((".jpg", ".png", ".gif")):
            # Try to extract image from Reddit preview or media metadata
            if hasattr(post, "preview"):
                image_url = post.preview["images"][0]["source"]["url"]
            elif hasattr(post, "media_metadata"):
                image_url = list(post.media_metadata.values())[0]["p"][0]["u"]
            else:
                continue  # Skip post if no valid image found
        
        # Avoid NSFW / Deleted content
        if not post.over_18:
            meme_data.append({
                "title": post.title,
                "score": post.score,
                "num_comments": post.num_comments,
                "created_utc": post.created_utc,
                "upvote_ratio": post.upvote_ratio,
                "url": image_url,  # Updated image URL
                "subreddit": sub
            })

# Convert to DataFrame
df = pd.DataFrame(meme_data)

# Save to CSV
df.to_csv("reddit_memes.csv", index=False)

print("✅ Data saved successfully! Check 'reddit_memes.csv'.")
