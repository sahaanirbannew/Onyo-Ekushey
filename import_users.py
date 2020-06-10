import global_ as g_ 
import numpy as np

def get_user_details(link):
    username = link.replace("https://twitter.com/","").strip() 
    user = api.get_user(username) 
    return user.name, user.screen_name

def write_to_trackers_list(type_, name, username):
    filename = './lists/'+type_+'.csv'
    file_write_to  = open(filename, "a+", encoding = 'utf-8')
    file_write_to.write(name + "," + username + "\n")
    g_.log_entry(name + "," + username + " added to the tracking list.", g_.const_info)
    file_write_to.close()
    
def import_by_link(link, type_): 
    name, username = get_user_details(link) 
    write_to_trackers_list(type_, name, username) 

def import_by_file(type_): 
    type_ = type_ + ".txt"   
    f = open(type_, "r") 
    list_accounts = f.read() 
    for link in list_accounts.split('\n'):  
        import_by_link(link, type_) 
    f.close() 

api = g_.setup() 
acceptable_type_s = ["politicians", "media", "industrialists", "sportspersons", "influencers"] 
mode = input("Single link or import from file? Possible Answers: [single | file]")
if mode == 'single':
        add_more = True
        while add_more == True:
            type_ = input("Choose --> Politicians | Media | Industrialists | Sportspersons | Influencers :").lower()
            if type_ not in acceptable_type_s:
                print("Please enter a valid option.")
            else:
                link = input("Enter the Twitter link: ").strip()
                import_by_link(link, type_)
                choice = input("Add another one? ").strip()
                if choice in ["yes","yea","ok"]:
                    add_more = True 
                else: 
                    add_more = False
if mode == 'file':
        type_ = input("Choose --> Politicians | Media | Industrialists | Sportspersons | Influencers :").lower()
        if type_ not in acceptable_type_s:
            g_.log_entry("This is not an acceptable name.", g_.const_error)
        else:
            import_by_file(type_)