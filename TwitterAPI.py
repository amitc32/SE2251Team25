import snscrape.modules.twitter as sntwitter
import pandas as pd
import billboardapi as bbp

class Twitter:
        def getTweets(title):
                
                q = title
                # Figure out how to Billboard.get song and artist name from Adams code
                # since searching generic takes too log to compile, gonna search song name and artist tweets

                 
                # add get locations, get date blah blah from team

                since_date = '2023-03-25'
                until_date = '2023-03-28'
                #Gonna change date, depending on relavance
                
                query = f'{q} since:{since_date} until:{until_date}' 
                # took location out of query since we are searching for song name and artist name better time complilation

                # Scraping...
                tweets = sntwitter.TwitterSearchScraper(query).get_items()
                num_tweets = len(list(tweets))

                return title, num_tweets

# create list of songs, gonna be taken from billboard classes    
tweet_list = bbp.billboardAPI()
# empty list that will hold song name/artist and tweets 
tweet_comp = []
# Call em'  
twitter = Twitter
for tweet in tweet_list:
        tweet_comp.append(twitter.getTweets(tweet))

print(tweet_comp)


# Create a Pandas DataFrame from the video data
columns = ["Song_Artist-Title","Song_Tweets"]
df = pd.DataFrame(tweet_comp, columns=columns)


# Sort songs
def rank_tweets(df):
    ranked_df = df.sort_values(by=['Song_Tweets'], ascending=False)
    ranked_df.reset_index(drop=True, inplace=True)
    return ranked_df
def sorted_tweets():
    return rank_tweets(df)
# print(sorted_tweets)
