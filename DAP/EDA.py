import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set up Seaborn for better visuals
sns.set(style="whitegrid", palette="pastel")

# Load the dataset
df = pd.read_csv("reddit_memes.csv")

# Display basic info
print("Dataset Overview:")
print(df.info())
print("\n")

# Display the first 5 rows
print("First 5 Rows:")
print(df.head())
print("\n")

# Check for missing values
print("Missing Values:")
print(df.isnull().sum())
print("\n")

# Basic statistics
print("Basic Statistics:")
print(df.describe())
print("\n")

# Unique subreddits
print("Unique Subreddits:")
print(df["subreddit"].value_counts())
print("\n")

# Convert 'created_utc' to datetime
df["created_utc"] = pd.to_datetime(df["created_utc"], unit="s")

# Add a 'day_of_week' column
df["day_of_week"] = df["created_utc"].dt.day_name()

# Add an 'hour' column
df["hour"] = df["created_utc"].dt.hour

# Plot 1: Distribution of Scores
plt.figure(figsize=(10, 6))
sns.histplot(df["score"], bins=50, kde=True, color="skyblue")
plt.title("Distribution of Post Scores", fontsize=16)
plt.xlabel("Score", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.show()

# Plot 2: Distribution of Upvote Ratios
plt.figure(figsize=(10, 6))
sns.histplot(df["upvote_ratio"], bins=20, kde=True, color="salmon")
plt.title("Distribution of Upvote Ratios", fontsize=16)
plt.xlabel("Upvote Ratio", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.show()

# Plot 3: Number of Posts per Subreddit
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="subreddit", palette="viridis")
plt.title(" Number of Posts per Subreddit", fontsize=16)
plt.xlabel("Subreddit", fontsize=12)
plt.ylabel("Number of Posts", fontsize=12)
plt.show()

# Plot 4: Average Score by Subreddit
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="subreddit", y="score", palette="magma", estimator=np.mean)
plt.title(" Average Score by Subreddit", fontsize=16)
plt.xlabel("Subreddit", fontsize=12)
plt.ylabel("Average Score", fontsize=12)
plt.show()

# Plot 5: Posts by Day of the Week
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="day_of_week", palette="coolwarm", order=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
plt.title("Posts by Day of the Week", fontsize=16)
plt.xlabel("Day of the Week", fontsize=12)
plt.ylabel("Number of Posts", fontsize=12)
plt.show()

# Plot 6: Posts by Hour of the Day
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="hour", bins=24, kde=True, color="purple")
plt.title("Posts by Hour of the Day", fontsize=16)
plt.xlabel("Hour of the Day", fontsize=12)
plt.ylabel("Number of Posts", fontsize=12)
plt.show()

# Plot 7: Correlation Heatmap
plt.figure(figsize=(10, 6))
corr = df[["score", "num_comments", "upvote_ratio"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title(" Correlation Heatmap", fontsize=16)
plt.show()

# Plot 8: Scatter Plot of Score vs. Number of Comments
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="score", y="num_comments", hue="subreddit", palette="deep")
plt.title("Score vs. Number of Comments", fontsize=16)
plt.xlabel("Score", fontsize=12)
plt.ylabel("Number of Comments", fontsize=12)
plt.show()

# Plot 9: Boxplot of Scores by Subreddit
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="subreddit", y="score", palette="Set3")
plt.title(" Distribution of Scores by Subreddit", fontsize=16)
plt.xlabel("Subreddit", fontsize=12)
plt.ylabel("Score", fontsize=12)
plt.show()

# Plot 10: Top 10 Most Upvoted Posts
top_posts = df.nlargest(10, "score")
plt.figure(figsize=(10, 6))
sns.barplot(data=top_posts, x="score", y="title", palette="rocket")
plt.title(" Top 10 Most Upvoted Posts", fontsize=16)
plt.xlabel("Score", fontsize=12)
plt.ylabel("Post Title", fontsize=12)
plt.show()

#Plot 11: Average Score by Day of the Week
plt.figure(figsize=(10, 6)) 
sns.barplot(data=df, x="day_of_week", y="score", palette="mako", estimator=np.mean, order=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
plt.title("Average Score by Day of the Week", fontsize=16)
plt.xlabel("Day of the Week", fontsize=12)
plt.ylabel("Average Score", fontsize=12)
plt.show()

# Beautiful charts

# Plot 12: Average Score by Hour of the Day
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="hour", y="score", palette="mako", estimator=np.mean)
plt.title("Average Score by Hour of the Day", fontsize=16)
plt.xlabel("Hour of the Day", fontsize=12)
plt.ylabel("Average Score", fontsize=12)
plt.show()

# Plot 13: Average Number of Comments by Subreddit
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="subreddit", y="num_comments", palette="viridis", estimator=np.mean)
plt.title("Average Number of Comments by Subreddit", fontsize=16)
plt.xlabel("Subreddit", fontsize=12)
plt.ylabel("Average Number of Comments", fontsize=12)
plt.show()

from wordcloud import WordCloud

text = " ".join(title for title in df["title"].astype(str))
wordcloud = WordCloud(width=800, height=400, background_color="white", colormap="coolwarm").generate(text)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Post Titles", fontsize=16)
plt.show()

# Plot 14: Word Cloud of Post Titles

plt.figure(figsize=(10, 6))
sns.violinplot(data=df, x="subreddit", y="score", palette="coolwarm", inner="quartile")
plt.title(" Violin Plot of Scores by Subreddit", fontsize=16)
plt.xlabel("Subreddit", fontsize=12)
plt.ylabel("Score", fontsize=12)
plt.show()

# Plot 16: Scatter Plot of Upvote Ratio vs. Score
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="upvote_ratio", y="score", hue="subreddit", palette="dark", alpha=0.7)
plt.title("Upvote Ratio vs. Score", fontsize=16)
plt.xlabel("Upvote Ratio", fontsize=12)
plt.ylabel("Score", fontsize=12)
plt.show()


# Plot 18: Pairplot of Numerical Features
sns.pairplot(df[["score", "num_comments", "upvote_ratio"]], diag_kind="kde", palette="coolwarm")
plt.suptitle("Pairplot of Numerical Features", fontsize=16)
plt.show()

# Plot 20: Donut Chart for Subreddit Distribution

subreddit_counts = df["subreddit"].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(subreddit_counts, labels=subreddit_counts.index, autopct="%1.1f%%", startangle=140, colors=sns.color_palette("pastel"), wedgeprops={"edgecolor": "black"})
plt.gca().add_artist(plt.Circle((0, 0), 0.6, fc="white"))
plt.title("istribution of Posts by Subreddit", fontsize=16)
plt.show()


