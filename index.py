from time import sleep
import datetime
import boto3, json, os, uuid, logging, random, string

from twitter import *

token = os.environ['TOKEN']
tokenSecret = os.environ['TOKEN_SECRET']
consumerKey = os.environ['CONSUMER_KEY']
consumerSecret = os.environ['CONSUMER_SECRET']

t = Twitter(
    auth=OAuth(token, tokenSecret, consumerKey, consumerSecret))

def lambda_handler(event, context):
    print(event)
    team_name = "my super awesome team"
    
    twitter_status = "team:"+team_name +" finished the #cloudnhl iOT challenge"


    print(twitter_status)
    
    try:
        t.statuses.update(status=twitter_status)
        return "Success"
    except Exception as e:
        print(e)
        return "Error"""
