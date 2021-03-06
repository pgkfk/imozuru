# -*- coding: utf-8 -*-
from flask import Flask, session, redirect, render_template, request, Response,jsonify  
import os
import tweepy
import sys
import json
app = Flask(__name__)

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
api = tweepy.API(auth)
app.secret_key = os.environ['SECRET_KEY']

keyword = ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/', methods=['POST'])
def search():
    json_data = request.get_json()
    global keyword
    keyword = json_data['keyword']
    if keyword:
        results=api.search(keyword,count=50)
        return  json.dumps([status._json for status in results])

    return  jsonify(json.dumps({'status':'NO','keyword':'no keyword'}))

@app.route('/pull/',methods=['POST'])
def pull():
    json_data = request.get_json()
    target_tweet_id = json_data['pull_id']
    target_status = api.get_status(target_tweet_id)
    later_tweets=api.user_timeline(target_status.author.id,since_id=target_tweet_id,count=25)
    earlier_tweets=api.user_timeline(target_status.author.id,max_id=target_tweet_id,count=25)
    result_tweets = []
    result_tweets.extend(later_tweets)
    result_tweets.extend(earlier_tweets)
    return  jsonify(json.dumps([status._json for status in result_tweets]))

if __name__ == '__main__':
    app.run(debug=True)
