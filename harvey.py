import json
import os

# i = 0
# for subdir, dirs, files in os.walk("E:\\Harvey\\Keyword_More"):
#     for file in files:
#         tweets = []
#         filepath = subdir + os.sep + file
#         print filepath
#         for line in open(filepath, 'r'):
#             try:
#                 line = json.loads(line)
#                 if line["place"] is not None and (line["place"]['country'] == "United States"):
#                     i+=1
#                     tweets.append(line)
#             except:
#                 continue
#         f = open("E:\\Harvey_new\\"+file, 'w+')
#         json.dump(tweets, f)


# print i, len(tweets)
# print tweets[100]

cities = ["Ganado", "La Ward", "Edna", "Anniston", "Glencoe", "Jacksonville", "Oxford", "Piedmont", \
            "Southside", "Weaver", "Austwell", "Alvin", "Angleton", "Brazoria", "Brookside Village" \
            "Clute"
,"Danbury"\
,"Freeport"\
,"Lake Jackson"\
,"Liverpool"\
,"Manvel"\
,"Oyster Creek"\
,"Pearland"\
,"Richwood"\
,"San Patricio"\
,"Gregory"\
,"Ingleside on the Bay"\
,"Mathis"\
,"Sandy Point"\
,"Surfside Beach"\
,"Sweeny"\
,"West Columbia"\
,"Aransas Pass "\
,"Corpus Christi "\
,"Ingleside"\
,"Portland"\
,"Odem"\
,"Sinton"\
,"Taft"\
, "Victoria"]
i = 0

for subdir, dirs, files in os.walk("C:\\Users\\akshdeep.r\\Documents\\FAI\\Project\\Harvey_Pre"):
    for file in files:
        tweets = []
        filepath = subdir + os.sep + file
        for tweet in json.load(open(filepath, 'r')):
            #print type(tweet["place"]['full_name'].encode('utf-8'))
            try:
                for city in cities:
                    if city in tweet["place"]['full_name'].encode('utf-8'):
                        print city
                        i+=1
                        tweets.append(tweet)
            except:
                continue
        f = open("C:\\Users\\akshdeep.r\\Documents\\FAI\\Project\\Harvey_Pre_New\\" +file, 'w+')
        json.dump(tweets, f)
