import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("YoutubeCommentsDataSet.csv", names=["text", "sentiment"])
df["sentiment"].value_counts().plot(kind="bar", color=["green", "red", "gray"])
plt.title("Sentiment Distribution")
plt.show()
