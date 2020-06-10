import fetch_tweets as fetch 
import global_ as g_ 
import time 
api = g_.setup() 

run_always = True 

while run_always == True:
    search_term  = input("Enter the seach term: ")
    last_fetched_id = g_.get_last_fetched_id(search_term) 
    tweets_table, last_fetched_id, error_message = fetch.fetch_tweets(api, "query", search_term, last_fetched_id)
    if len(tweets_table)>0: 
        g_.dump_file(search_term, tweets_table)
        g_.update_last_fetched(search_term, last_fetched_id)
        g_.log_entry(str(len(tweets_table))+" tweets for search term "+str(search_term), g_.const_info)
        
        for tweet in tweets_table:
            print(tweet[3])
            print("========")
    else:
        g_.log_entry("No new tweets for search term "+str(search_term), g_.const_info)
    time.sleep(300)