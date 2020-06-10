import fetch_tweets as fetch 
import global_ as g_ 
import time 
api = g_.setup() 

run_always = True 

while run_always == True:

    users_list_file = open("./lists/politicians.csv", "r", encoding="utf-8") 
    users_list = users_list_file.read()    
    """
    Guide: 
    tweets_table, last_fetched_id, error_message = fetch_tweets(api, "username", username, last_id)
    tweets_table, last_fetched_id, error_message = fetch_tweets(api, "newsfeed", '', last_id)
    tweets_table, last_fetched_id, error_message = fetch_tweets(api, "query", query, last_id)
    """ 
    for user in users_list.split("\n"):
        if len(user)>0:
            full_name = user.split(",")[0]
            username = user.split(",")[1] 
            last_fetched_id = g_.get_last_fetched_id(username) 
            tweets_table, last_fetched_id, error_message = fetch.fetch_tweets(api, "username", username, last_fetched_id)
            if len(tweets_table)>0: 
                g_.dump_file(username, tweets_table)
                g_.update_last_fetched(username, last_fetched_id)
                g_.log_entry(str(len(tweets_table))+" tweets from "+str(full_name), g_.const_info)
            else:
                g_.log_entry("No new tweets from "+str(full_name), g_.const_info)
    time.sleep(300)