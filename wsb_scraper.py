# Pulls 1000 new post from Wall Street Bets
# https://www.reddit.com/pref/apps

import praw
import pandas as pd
import datetime
from reddit_key import *



reddit = praw.Reddit(client_id = get_client_id(),
                     client_secret= get_client_secret(),
                     user_agent= get_user_agent(),
                     username= get_username(),
                     password= get_password(),
    )



subreddit = reddit.subreddit('wallstreetbets')

top_subreddit = subreddit.new(limit=1000)

#def get_date(submission):
    #time = submission.created
    #return datetime.datetime.fromtimestamp(time)


words_collection = []
time_posted = []

for submission in top_subreddit:
    created = datetime.datetime.fromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S')
    submission_id = submission.id
    title = submission.title
    title_words = title.split()
    words_collection.append(title_words)
    time_posted.append(created)

out = [item for item in words_collection if map(str.isupper, item)]

content = pd.DataFrame(zip(out))
timestamp = pd.DataFrame(zip(time_posted))

df = pd.merge(timestamp,content, left_index = True, right_index = True)

df = df.rename(columns={'0_x':'time','0_y':'post_content'})

wsb_new_post = df

def get_dataframe_wsb_new_post():
    wsb_new_post
    return wsb_new_post


#Check overall data via csv
#df.to_csv(r'C:\Users\Ryan Levey\OneDrive\Bureaublad\DE Project\stockhype\wsb_post_new.csv')