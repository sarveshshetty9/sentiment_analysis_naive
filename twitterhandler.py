import csv
import os
import pandas as pd

import re
import converter as conv
import cleaner as clr
import usersentencedivert as usd
import twitterhandler as twk
def dataextraction(s2):
    import tweepy

    from tweepy.streaming import StreamListener
    from tweepy import OAuthHandler
    from tweepy import Stream
    import json
    import time
    import pandas as pd
    
    access_token = "1085460732727050241-HFKwiRJtEjFQcuFzLuIEQVo3072LPw"
    access_secret = "L9ltIAi8F49ywLItCPPNMuQEOwkGOaqsYtVHgznX8Tf6S"
    consumer_key = "z4b4IalHycnih8SB951QeSeCT"
    consumer_secret = "6EcfdQmoppfZQzobMBUSREwLI4vBZTI8QFXnIWuy7Aepw2dyJS"
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    searchquery = s2
    users =tweepy.Cursor(api.search,q=searchquery).items()
    count = 0
    start = 0
    errorCount=0
    waitquery = 100      #this is the number of searches it will do before resting
    waittime = 2.0          # this is the length of time we tell our program to rest
    total_number = 10   #this is the total number of queries we want
    justincase = 1         #this is the number of minutes to wait just in case twitter throttles us
    text = [1] * total_number
    secondcount = 0
    idvalues = [1] * total_number
    while secondcount < total_number:
        try:
            user = next(users)
            count += 1
            if (count%waitquery == 0):
                time.sleep(waittime + 5)
        except tweepy.TweepError:
            print ("sleeping....")
            time.sleep(justincase)
            user = next(users)
        except StopIteration:
            break
        try:
            text_value = user._json['text']
            language = user._json['lang']        #print(text_value)
            print(language)
            if "RT" not in text_value:
                if language == "en":
                    text[secondcount] = text_value
                    secondcount = secondcount + 1
                    print("current saved is:")
                    percent=secondcount/2
                    print(percent)
        except UnicodeEncodeError:
            errorCount += 1
            print ("UnicodeEncodeError,errorCount ="+str(errorCount))


    print("Creating dataframe:")

    d = {"text": text}
    df = pd.DataFrame(data = d)
    if os.path.exists('sample.csv'):
        os.remove('sample.csv')
    df.to_csv('sample.csv', header=True, index=False, encoding='utf-8')

    print ("completed")
    list1=[]
    with open('sample.csv', 'r') as f:
        reader = csv.reader(f)
        list1 = list(reader)
    k=len(list1)
    list2=[]
    for i in range(k):
        list2.append(i)
    filename = "sample.csv"
    fields = ['id', 'review'] 
# writing to csv file 
    with open(filename, 'w') as csvfile: 
    # creating a csv dict writer object 
        writer = csv.DictWriter(csvfile, fieldnames = fields) 
      
    # writing headers (field names) 
        writer.writeheader() 
      


        for i in range(1,k):
            mydict =[{'id':i, 'review': list1[i]}]
            writer.writerows(mydict)
        
    conv.convertcsvtotsv()
    conv.refurbish()
