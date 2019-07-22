import sklearn
import pickle
import praw
import re
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords

reddit = praw.Reddit(client_id='#', client_secret='#', user_agent='#', username='#', password='#')

remove_space = re.compile('[/(){}\[\]\|@,;]')
Remove_Symbols = re.compile('[^0-9a-z #+_]')
STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
   
    text = BeautifulSoup(text, "lxml").text
    text = text.lower()
    text = remove_space.sub(' ', text)
    text = Remove_Symbols.sub('', text)
    text = ' '.join(word for word in text.split() if word not in STOPWORDS)
    return text

def detect_flair(url,loaded_model):

  submission = reddit.submission(url=url)

  redditt = {}

  redditt['title'] = submission.title
  redditt['url'] = submission.url

  submission.comments.replace_more(limit=None)
  comment = ''
  for top_level_comment in submission.comments:
    comment = comment + ' ' + top_level_comment.body
  redditt["comment"] = comment
  redditt['comment'] = clean_text(redditt['comment'])
  redditt['title'] = clean_text(redditt['title'])
  redditt['main'] = redditt['title'] + redditt['comment'] + redditt['url']
  
  return loaded_model.predict([redditt['main']])
