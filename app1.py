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

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if 'keyword' in request.form:
            global keyword
            keyword = request.form['keyword']
            if keyword:
                return render_template(
                    'index.html',
                    keyword=keyword,
                    result=api.search(keyword,count=50)
                    )
        # if 'pull' in request.form:
        #     target_tweet_id = request.form['pull']
        #     target_status = api.get_status(target_tweet_id)
        #     # print target_tweet_id
        #     # later_tweets=api.user_timeline(target_status.author.id,since_id=target_tweet_id,count=10)
        #     earlier_tweets=api.user_timeline(target_status.author.id,max_id=target_tweet_id,count=1)
        #     # return  jsonify(json.dumps([status._json for status in earlier_tweets]))
            # return  jsonify(json.dumps({'status':'OK','user':'kb'}))
            # return render_template(
            #     'index.html',
            #     keyword=keyword,
            #     result=api.search(keyword,count=50),
            #     later_tweets=api.user_timeline(target_status.author.id,since_id=target_tweet_id,count=10),
            #     earlier_tweets=api.user_timeline(target_status.author.id,max_id=target_tweet_id,count=10)
            #     )
    print 'hsssge'
    return render_template('index.html')

@app.route('/pull',methods=['POST'])
def pull():
    print request.form
    print 'hoge'
    return  jsonify(json.dumps({'status':'OK','user':'kb'}))
if __name__ == '__main__':
    app.run(debug=True)