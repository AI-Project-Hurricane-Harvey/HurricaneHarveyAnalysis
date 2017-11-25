import os
import json


i = 0
users_set_pre_evacuation = set()
for subdir, dirs, files in os.walk("C:\\Users\\kevin\\Desktop\\Masters\\Semester 1\\FAI\\Project\\Harvey_pre_evacuation_final"):
    for file in files:
        filepath = subdir + os.sep + file
        try:
            for tweet in json.load(open(filepath, 'r')):
            #users_set.add(tweet["user"]["id"])
                users_set_pre_evacuation.add(tweet["user"]["id"])
        except:
            print file
            continue 
print len(users_set_pre_evacuation)


i = 0
users_set_post_evacuation = set()
for subdir, dirs, files in os.walk("C:\\Users\\kevin\\Desktop\\Masters\\Semester 1\\FAI\\Project\\Harvey_post_evacuation_final"):
    for file in files:
        filepath = subdir + os.sep + file
        try:
            for tweet in json.load(open(filepath, 'r')):
            #users_set.add(tweet["user"]["id"])
                users_set_post_evacuation.add(tweet["user"]["id"])
        except:
            print file
            continue 
print len(users_set_post_evacuation)

common_users = []
common_users = users_set_pre_evacuation.intersection(users_set_post_evacuation)
print len(common_users)


all_user_tweets_post = {}

for userid in common_users:
    all_user_tweets_post[userid] = []
    
for subdir, dirs, files in os.walk("C:\\Users\\kevin\\Desktop\\Masters\\Semester 1\\FAI\\Project\\Harvey_post_evacuation_final"):
    for file in files:
        filepath = subdir + os.sep + file
        for tweet in json.load(open(filepath, 'r')):    
            if (tweet["user"]["id"] in common_users):
                all_user_tweets_post[tweet["user"]["id"]].append(tweet)

f = open("C:\\Users\\kevin\\Desktop\\Masters\\Semester 1\\FAI\\Project\\common_user_post_tweets.json", 'w+')
json.dump(all_user_tweets_post, f) 

print all_user_tweets_post