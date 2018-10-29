import tweepy
import csv

from config import consumer_key, consumer_secret, access_token, access_token_secret # edit config with your own twitter api key

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def hashAnalysis(hashtag):
    print("Pulling tweets from {}\n".format(hashtag))
    data = []
    
    with open('tweets.csv','w', encoding='UTF-8', newline='') as csvArchive:
        writer=csv.writer(csvArchive)
        for tweet in tweepy.Cursor(api.search, q = hashtag, rpp = 100).items(100):
            try: # this handles unknown characters. which are skipped i.e emojis
                if(tweet.text[:2] == 'RT'): # eliminates third part retweet application 
                    pass
                else:
                    if(tweet.text not in data):
                        data.append(tweet.text) 
                        writer.writerow([tweet.text])
            except: 
                pass

    # # writes tweets to a csv file
    # with open('tweets.csv','w', encoding='UTF-8', newline='') as csvArchive:
    #     writer=csv.writer(csvArchive)
    #     for val in data:
    #         writer.writerow([val])
   
    print("Tweets have been pulled")


