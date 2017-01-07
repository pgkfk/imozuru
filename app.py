from flask import Flask, session, redirect, render_template, request
import os
import tweepy
import sys


app = Flask(__name__)

app.config.from_object('config')

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
oauth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_SECRET = os.environ['ACCESS_SECRET']
oauth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(oauth)

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
                imozuru_since_tweet=api.user_timeline(target_status.author.id,since_id=target_tweet_id,count=10),
                imozuru_max_tweet=api.user_timeline(target_status.author.id,max_id=target_tweet_id,count=10))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)