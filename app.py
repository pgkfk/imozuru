# -*- coding: utf-8 -*-
from flask import Flask, session, redirect, render_template, request
import os
import tweepy
import sys


app = Flask(__name__)
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

api = tweepy.API(auth)
app.secret_key = os.environ['SECRET_KEY']



@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if 'keyword' in request.form:
            keyword = request.form['keyword']
            if keyword:
                return render_template(
                    'index.html',
                    keyword=keyword,
                    result=api.search(keyword,count=50)
                    )
        if 'pull' in request.form:
            target_tweet_id = request.form['pull']
            target_status = api.get_status(target_tweet_id)
            return render_template(
                'index.html',
                later_tweets=api.user_timeline(target_status.author.id,since_id=target_tweet_id,count=10),
                earlier_tweets=api.user_timeline(target_status.author.id,max_id=target_tweet_id,count=10)
                )

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)