import tweepy
import time
import pickle

def fetch_tweets(api, by_what, username_or_query, last_id):
  tweets_table = []
  tweets_table, error_message, last_fetched_id = init_params()   
  try: 
    if by_what == 'username': 
        username = username_or_query 
        tweets_table, last_fetched_id = create_tweets_table(api.user_timeline(username), last_id) 
    elif by_what == 'newsfeed':
        tweets_table, last_fetched_id = create_tweets_table(api.home_timeline(), last_id)
    elif by_what == 'query': 
        query = username_or_query 
        tweets_table, last_fetched_id = create_tweets_table(api.search(query), last_id) 
    else: 
        g_.log_entry("The user needs to enter how s/he wants to fetch tweets.", g_.const_error) 
  except Exception as e:
    error_message = str(e) 
    return [], 0, error_message  
  
  return tweets_table, last_fetched_id, error_message 
  
  
def single_tweet_details(tweet):
  single_tweet_details_array = [tweet.created_at, "@" + tweet.user.screen_name, tweet.id, tweet.text, tweet.entities['hashtags'], tweet.entities['user_mentions']]
  return single_tweet_details_array
    
def init_params():
    return [], '', 0 

def create_tweets_table(public_tweets, last_id):
    tweets_table = [] 
    last_fetched_id = public_tweets[0].id  
    for tweet in public_tweets:
        if tweet.id > last_id:
            single_tweet_details_array = single_tweet_details(tweet) 
            tweets_table.append(single_tweet_details_array)
    return tweets_table, last_fetched_id