# import tweepy
import json
import requests
from datetime import date, timedelta


def getTweets(keyword):
  # Authentication 
  bearer_token = 'AAAAAAAAAAAAAAAAAAAAAPC3jAEAAAAAlfohKzVAUpkPrPYyUnsp9P5BNQE%3D4dTdbGWEW04ksJ653bieS37UwKOeZGRGe3Ib5Z6hcyhJjQDaFh'
  client = tweepy.Client(bearer_token)

  # Query tweets from twitter by Tweepy
  query = keyword
  res = client.search_recent_tweets(query, max_results=100)
  print(res.meta)
  data = []
  for tweet in res.data:
    data.append(tweet.text)
  return data
  
def getNews(keyword):
  apikey = '6877008d158c42fea587ed433ffb244c'
  url = ('https://newsapi.org/v2/everything?q=' + keyword 
         + '&language=en&from=' + str(date.today() - timedelta(days=3))  
         + "&to=" + str(date.today()) + '&sortBy=popularity&apiKey=' + apikey)
  print(url)

  response = requests.get(url)
  articles = response.json()['articles']
  data = []
  for article in articles:
    text = article['title']
    if article['description'] != None:
      text += " | " + article['description'] 
    if article['content'] != None:
      text += " | " + article['content']
    data.append((text, article['url']))
  print("Called everything API, data length:" + str(len(data)))
  print(data[0])
  return data

def getHeadlines():
  apikey = '6877008d158c42fea587ed433ffb244c'
  url ='https://newsapi.org/v2/top-headlines?country=us&apiKey=' + apikey
  response = requests.get(url)
  articles = response.json()['articles']
  data = []
  for article in articles:
    text = article['title']
    if article['description'] != None:
      text += " | " + article['description'] 
    if article['content'] != None:
      text += " | " + article['content']
    data.append((text, article['url']))
  print("Called top headline API, data length:" + str(len(data)))
  print(data[0])
  return data