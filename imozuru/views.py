from imozuru import app
from flask import Flask, session, redirect, render_template, request
import os
import tweepy
import sys
# import twitter

# api = ''
# isfirst=True
# def initialize():
SECRET_KEY = os.environ['SECRET_KEY']
WTF_CSRF_ENABLED = True
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_SECRET = os.environ['ACCESS_SECRET']
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
# global api
api = tweepy.API(auth)
# isfirst=False
    # api = twitter.Api(consumer_key=os.environ['CONSUMER_KEY'],
    #                   consumer_secret=os.environ['CONSUMER_SECRET'],
    #                   access_token_key=os.environ['ACCESS_TOKEN'],
    #                   access_token_secret=os.environ['ACCESS_SECRET']
    #                   )


@app.route('/',methods=['GET','POST'])
def index():
    # if isfirst:
    #     initialize()

    if request.method == 'POST':
        if 'keyword' in request.form:
            keyword = request.form['keyword']
            if keyword:
                return render_template(
                    'index.html',
                    keyword=keyword,
                    result=api.search(keyword,count=50))
        if 'pull' in request.form:
            target_tweet_id = request.form['pull']
            target_status = api.get_status(target_tweet_id)
            return render_template(
                'index.html',
                imozuru_since_tweet=api.user_timeline(target_status.author.id,since_id=target_tweet_id,count=10),
                imozuru_max_tweet=api.user_timeline(target_status.author.id,max_id=target_tweet_id,count=10))
    # api.PostUpdate("tweet from my app")

    return render_template('index.html')