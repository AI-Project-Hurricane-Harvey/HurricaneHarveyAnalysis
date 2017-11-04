import json
import os

i = 0
for subdir, dirs, files in os.walk("E:\\Harvey\\Keyword_More"):
    for file in files:
        tweets = []
        filepath = subdir + os.sep + file
        print filepath
        for line in open(filepath, 'r'):
            try:
                line = json.loads(line)
                if line["place"] is not None and (line["place"]['country'] == "United States"):
                    i+=1
                    tweets.append(line)
            except:
                continue
        f = open("E:\\Harvey_new\\"+file, 'w+')
        json.dump(tweets, f)


print i, len(tweets)
print tweets[100]
