import TwitterAPI as Twitter
import Youtube as Youtube
import billboardapi as bbd
import pandas as pd

class Formatter:

    # creating fields for the output of the twitter and youtube data, and calling the fuctions
    tw = Twitter.sorted_tweets()
    yt = Youtube.sorted_songs()

    def parseResults():

        # converting the dataframes into lists of tuples to append positions to them
        tweets = list(Formatter.tw)
        views = list(Formatter.yt)

        # setting default positioning
        tweets_pos = 1

        # adding positioning to results
        for twiiter_results in tweets:
            twiiter_results.append(tweets_pos)
            tweets_pos += 1

        # setting default positioning
        watch_pos = 1
        
        # adding positioning to results
        for youtube_results in views:
            youtube_results.append(watch_pos)
            watch_pos += 1

        # setting default positioning
        song_pos = 1

        # parsing a list containing each song title and their ranking on twitter, youtube and billboard
        ranked_song_list = []
        for billboard_entry in bbd.billboardApi.run():
            song_info = billboard_entry
            pos = song_pos
            song_pos += 1
            
            for twiiter_results in tweets:
                if twiiter_results[0] == song_info:
                    twitter_score = twiiter_results[2]
                    break
           
            for youtube_results in views:
                if youtube_results[0] == song_info:
                    youtube_score = twiiter_results[6]
                    break

            ranked_song = (billboard_entry,pos,twitter_score,youtube_score)   
            ranked_song_list.append(ranked_song)
        return ranked_song_list

    def twiiterAccuracy():

        # calls to parse the results
        ranked_song_list = Formatter.parseResults()
        tweet_accuracy = []
        twiiter_accuracy = 1

        # checks the relative distance between the different results and creates an accuracy score
        for song in ranked_song_list:
            if song[1] > song[2]:
                twiiter_accuracy = (len(bbd.billboardAPI.run()) - (song[1]-song[2]))/len(bbd.billboardAPI.run())
            elif song[1] < song[2]:
                twiiter_accuracy = (len(bbd.billboardAPI.run()) - (song[2]-song[1]))/len(bbd.billboardAPI.run())

            artist_and_song = song[0].split(' AND ')
            artist = artist_and_song[0]
            title = artist_and_song[1]
    
            tweet_specs = (artist,title,twiiter_accuracy)
            tweet_accuracy.append(tweet_specs)
            twitter_accuracy += 1
        return tweet_accuracy

    def youtubeAccuracy():

        # calls to parse the results
        ranked_song_list = Formatter.parseResults()
        views_accuracy = []
        youtube_accuracy = 1

        # checks the relative distance between the different results and creates an accuracy score
        for song in ranked_song_list:
            if song[1] > song[3]:
                youtube_accuracy = (len(bbd.billboardAPI.run()) - (song[1]-song[3]))/len(bbd.billboardAPI.run())
            elif song[1] < song[3]:
                youtube_accuracy = (len(bbd.billboardAPI.run()) - (song[3]-song[1]))/len(bbd.billboardAPI.run())
            
            artist_and_song = song[0].split(' AND ')
            artist = artist_and_song[0]
            title = artist_and_song[1]

            views_specs = (artist,title,youtube_accuracy)
            views_accuracy.append(views_specs)
            views_accuracy += 1
        return views_accuracy

    def billboardAccuracy():

        # calls to parse the results
        ranked_song_list = Formatter.parseResults()
        twitter_accuracy = Formatter.twiiterAccuracy()
        youtube_accuracy = Formatter.youtubeAccuracy()
        percentage = "{:.2%}"
        song_pos = 0
        billboard_accuracy = []

        # checks the relative distance between the different results and creates an accuracy score
        for song_entry in ranked_song_list:
            ranking_accuracy = (twitter_accuracy[song_pos][1] + youtube_accuracy[song_pos][1])/2

            artist_and_song = song_entry[0].split(' AND ')
            artist = artist_and_song[0]
            title = artist_and_song[1]

            billboard_accuracy.append(artist,title,percentage.format(twitter_accuracy[song_pos][1]),percentage.format(youtube_accuracy[song_pos][1]),percentage.format(ranking_accuracy))
            song_pos += 1
        return billboard_accuracy

    def formatAllValues():
        # calls together all prior methods and creates a data frame with all of the accuracy scores
        ranked_list = Formatter.billboardAccuracy()
        titles = ['Artist','Title','Twitter Accuracy','Youtube Accuracy','Billboard Accuracy']
        formatted_output = pd.DataFrame(ranked_list,columns=titles)
        return formatted_output

class OutputFormattedInformation:
    
    def printByBillboard():
        print(Formatter.formatAllValues())

    def printByBillboardAccuracy():
        print("Printed by Billboard Accuracy")
        ranked_by_billboard_accuracy = Formatter.formatAllValues().sort_values(by=['Billboard Accuracy'], ascending=False)
        print(ranked_by_billboard_accuracy)

    def printByTwitterAccuracy():
        print("Printed by Twiiter Accuracy")
        ranked_by_billboard_accuracy = Formatter.formatAllValues().sort_values(by=['Twitter Accuracy'], ascending=False)
        print(ranked_by_billboard_accuracy)

    def printByYoutubeAccuracy():
        print("Printed by Youtube Accuracy")
        ranked_by_billboard_accuracy = Formatter.formatAllValues().sort_values(by=['Youtube Accuracy'], ascending=False)
        print(ranked_by_billboard_accuracy)

# commands to run to output all relative accuracies in their sorted orders
print("Billboard Hot-100 list:")
print(bbd.billboardAPI.run() + "\n"*3)
print("Tweet's regarding each song in order of their tweet count:")
print(Formatter.tw + "\n"*3)
print("Youtube streams for each song in order of their views, likes and comments:")
print(Formatter.yt + "\n"*3)
print("Billboard Hot-100 list ordered by billboards natural order of popularity:")
OutputFormattedInformation.printByBillboard()
print("\n"*3)
print("Billboard Hot-100 list ordered by billboards accuracy to both twitter and youtube:")
OutputFormattedInformation.printByBillboardAccuracy()
print("\n"*3)
print("Billboard Hot-100 list ordered by twitters accuracy to the billboard:")
OutputFormattedInformation.printByTwitterAccuracy()
print("\n"*3)
print("Billboard Hot-100 list ordered by youtubes accuracy to the billboard:")
OutputFormattedInformation.printByYoutubeAccuracy()
