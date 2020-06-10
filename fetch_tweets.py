import tweepy
import time
import pickle
import global_ as g_


def get_count(last_id):
    if last_id>0:
        return 20
    else:
        return 500
    pass


def fetch_tweets(api, by_what, username_or_query, last_id):
    tweets_table = []
    tweets_table, error_message, last_fetched_id = init_params()
    count = get_count(last_id)
    try:
        if by_what == 'username':
            username = username_or_query
            tweets_table, last_fetched_id = create_tweets_table(api, api.user_timeline(username, tweet_mode='extended', count = count), last_id)
        elif by_what == 'newsfeed':
            tweets_table, last_fetched_id = create_tweets_table(api, api.home_timeline(tweet_mode='extended', count = count), last_id)
        elif by_what == 'query':
            query = username_or_query
            tweets_table, last_fetched_id = create_tweets_table(api, api.search(query, tweet_mode='extended', count = count), last_id)
        else:
            g_.log_entry("The user needs to enter how s/he wants to fetch tweets.", g_.const_error)
    except Exception as e:
        error_message = str(e)
        return [], 0, error_message

    return tweets_table, last_fetched_id, error_message


def get_full_text_by_tweet_id(api, id):
    tweet = api.get_status(id=id, tweet_mode="extended")
    if 'extended_tweet' in tweet._json:
        tweet_text = tweet._json['extended_tweet']['full_text']
    else:
        tweet_text = tweet.full_text
    return tweet_text


def single_tweet_details(api, tweet):
    if 'extended_tweet' in tweet._json:
        tweet_text = tweet._json['extended_tweet']['full_text']
    else: 
        tweet_text = tweet.full_text

    print(tweet_text)
    print(tweet_text[0:2])
    print(tweet_text[-1:])
    if tweet_text[-1] == '…' and tweet_text[0:2] == 'RT':
        source_tweet_id = tweet.retweeted_status.id
        tweet_text = get_full_text_by_tweet_id(api, source_tweet_id)

    single_tweet_details_array = [tweet.created_at, "@" + tweet.user.screen_name, tweet.id, tweet_text,
                                  tweet.entities['hashtags'], tweet.entities['user_mentions']]
    return single_tweet_details_array


def init_params():
    return [], '', 0


def create_tweets_table(api, public_tweets, last_id):
    tweets_table = []
    last_fetched_id = public_tweets[0].id
    for tweet in public_tweets:
        if tweet.id > last_id:
            single_tweet_details_array = single_tweet_details(api, tweet)
            tweets_table.append(single_tweet_details_array)
    return tweets_table, last_fetched_id
