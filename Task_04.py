import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Twitter training dataset
twitter_training_file_path = 'twitter/twitter_training.csv'
twitter_training_data = pd.read_csv(twitter_training_file_path, header=None)

# Extract the sentiment column for analysis (Column 2 contains the sentiment labels)
sentiment_counts = twitter_training_data[2].value_counts()

# Plot the sentiment distribution
plt.figure(figsize=(8, 6))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette="viridis")
plt.title('Sentiment Distribution in Twitter Data')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()
