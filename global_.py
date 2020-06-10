from datetime import datetime 
import pickle 
import tweepy
const_info = '[ Info]'
const_error = '[Error]'

def log_entry(text, msg_type):
    log_path = 'log.txt'
    try:
        log_file = open(log_path, 'a+', encoding="utf-8")
    except:
        log_file = open('log.txt', 'a+', encoding="utf-8")
    time_string = get_time_string()
    log_file.write(time_string + ' ' + msg_type + ' :' + text + '\n')
    log_file.close()
    print(time_string + ' ' + msg_type + ' :' + text)


def get_time_string():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

def dump_file(term, table):
    time_string = get_time_string()
    term = term.replace(" ","_") 
    file_path = "./dump_tweets/"+term + "_" + str(time_string).replace(":","-")+".pkl" 
    f = open(file_path, "wb")
    pickle.dump(table, f) 

def get_last_fetched_id(username):
    file_path = "last_updated.pkl" 
    try:
        with open(file_path, 'rb') as file:
            last_updated = pickle.load(file)
        if username in last_updated:
            return last_updated[username]
        else:
            return 0 
    except:
        return 0

def update_last_fetched(username, last_id):
    file_path = "last_updated.pkl" 
    try:
        with open(file_path, 'rb') as file:
            last_updated = pickle.load(file)
    except:
        last_updated = {} 
        
    if username in last_updated:
        last_updated[username] = last_id 
    else: 
        last_updated[username] = last_id 
    
    pickle.dump(last_updated, open(file_path, "wb")) 
    
def setup():
  consumer_key = "iPaIdR8GRI59yTJMs0Es0dIBN"
  consumer_secret = "pLadg3UaLeK3yKDujRMChRN3p8hUDBOjBsuOBy8j8ERr4zz1vs"
  access_token = "39085479-AabHt6bmFSbClDfUZuHjModYPAxVlOxHeMA79UyVt"
  access_token_secret = "3IqXDISfqg14wzMNNn2AX4KYG9Wfkltt21QxKasE4YNnG"
  # Creating the authentication object
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  # Setting your access token and secret
  auth.set_access_token(access_token, access_token_secret)
  # Creating the API object while passing in auth information
  api = tweepy.API(auth) 
  return api
    