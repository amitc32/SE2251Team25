import snscrape.modules.twitter as sntwitter
import pandas as pd

class Twitter:
        def getTweets(title):
                
                q = title
                # Figure out how to Billboard.get song and artist name from Adams code
                # since searching generic takes too log to compile, gonna search song name and artist tweets

                location = 'Canada' 
                # add get locations, get date blah blah from team

                since_date = '2023-03-1'
                until_date = '2023-03-28'
                #Gonna change date, depending on relavance
                
                query = f'{q} since:{since_date} until:{until_date}' 
                # took location out of query since we are searching for song name and artist name better time complilation

                # Scraping...
                tweets = sntwitter.TwitterSearchScraper(query).get_items()
                num_tweets = len(list(tweets))

                return title, num_tweets

# create list of songs, gonna be taken from billboard classes    
tweet_list = ["Morgan Wallen AND Whiskey Glasses", "Ice Spice AND Boys a Liar", "Lilbaby AND Grace"]
# empty list that will hold song name/artist and tweets 
tweet_comp = []
# Call em'  
twitter = Twitter
for tweet in tweet_list:
        tweet_comp.append(twitter.getTweets(tweet))

print(tweet_comp)


df = pd.DataFrame()

