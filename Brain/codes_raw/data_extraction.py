# -*- coding: utf-8 -*-
"""data_extraction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18k3UTWGd-PFyX2D797Jsb0mQqql9qb1O
"""

!pip install praw
import praw
import pandas as pd
import datetime as dt



subreddit = reddit.subreddit('India')

top_subreddit = subreddit.top()

top_subreddit = subreddit.top(limit=1000)
print(top_subreddit)

for submission in subreddit.top(limit=1):
    print(submission.title, submission.id)

topics_dict = { "author":[], \
                "body":[], \
                "comments":[], \
                "comms_num":[], \
                "flair": [], \
                "id": [], \
                "score":[], \
                "title": [], \
                "url": [], \
                "timestamp":[]}

for submission in top_subreddit:
    topics_dict["author"].append(submission.author)
    topics_dict["body"].append(submission.selftext)
    topics_dict["comments"].append(submission.comments)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["flair"].append(submission.link_flair_text)
    topics_dict["id"].append(submission.id)
    topics_dict["score"].append(submission.score)
    topics_dict["title"].append(submission.title)
    topics_dict["url"].append(submission.url)

dict_df = pd.DataFrame({ key:pd.Series(value) for key, value in topics_dict.items() })

df.to_csv("data.csv")