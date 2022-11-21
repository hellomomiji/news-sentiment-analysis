import os
import collections
from transformers import pipeline
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

plt.switch_backend('Agg')

def sentimentAnalysis(data):
  # # Set up the inference pipeline using a model from the 🤗 Hub
  sentiment_analysis = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion')
  
  #run the sentiment analysis on each text
  results = []
  for d in data:
    try:
      sentiments = sentiment_analysis(d)
      top_sentiment = max(sentiments, key=lambda x:x['score'])
      results.append(top_sentiment['label'])
    except:
      pass
  sentiment_counts = sorted(collections.Counter(results).items(), key=lambda pair:pair[1], reverse=True)
  print(sentiment_counts)
  return sentiment_counts #type: list of tuples list[(sentiment, count)]
  
def generateWordCloud(data, keyword):
  # Wordcloud with news
  words = data
  stop_words = ["https", "co", "RT","...", "|", "BBC", "CNN", "Reuters", keyword] + list(STOPWORDS)
  wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white", stopwords = stop_words).generate(str(words))
  plt.figure()
  plt.title(keyword + " Wordcloud")
  plt.imshow(wordcloud, interpolation="bilinear")
  plt.axis("off")
  img_path = 'static/img/wordcloud.png'
  plt.savefig(img_path)
  plt.close()

def generateGraph(sentiments_counts):
    # convert to pandas dataframe
    df = pd.DataFrame(sentiments_counts, columns=['sentiment', 'count'])
    # visualize the sentiments
    fig = plt.figure(figsize=(6,6), dpi=100)
    ax = plt.subplot(111)
    labels = df['sentiment'].values.tolist()
    print(labels)
    df.plot.pie(ax=ax, autopct='%1.1f%%', startangle=270, fontsize=12, labels=labels, y="count")
    graph_path = 'static/img/graph.png'
    plt.savefig(graph_path)
    plt.close()
  
def getGraphPath():
    return 'static/img/graph.png'

def getImgPath():
  return 'static/img/wordcloud.png'
