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

    def process_tweets():
        # create list of songs, gonna be taken from billboard classes    
        ### tweet_list = bbd.billboardAPI.run()
        # empty list that will hold song name/artist and tweets 
        ### tweet_comp = []
        # Call em'  
        ### twitter = Twitter
        ### for tweet in tweet_list:
            ### tweet_comp.append(twitter.getTweets(tweet))
        tweet_comp = [('Miley Cyrus AND Flowers', 1211), ('Morgan Wallen AND Last Night', 113), ('SZA AND Kill Bill', 765), ("Metro Boomin, The Weeknd & 21 Savage AND Creepin'", 116), ('The Weeknd & Ariana Grande AND Die For You', 156), ("PinkPantheress & Ice Spice AND Boy's A Liar, Pt. 2", 69), ('Taylor Swift AND Anti-Hero', 497), ('Rema & Selena Gomez AND Calm Down', 164), ('Coi Leray AND Players', 351), ('Bailey Zimmerman AND Rock And A Hard Place', 11), ('Morgan Wallen AND Thought You Should Know', 19), ('Taylor Swift AND All Of The Girls You Loved Before', 228), ('Morgan Wallen AND You Proof', 11), ('Chris Brown AND Under The Influence', 179), ('Harry Styles AND As It Was', 342), ("David Guetta & Bebe Rexha AND I'm Good (Blue)", 96), ('Taylor Swift AND Lavender Haze', 161), ('Sam Smith & Kim Petras AND Unholy', 139), ('Lil Uzi Vert AND Just Wanna Rock', 108), ("Morgan Wallen AND Thinkin' Bout Me", 8), ('Toosii AND Favorite Song', 235), ('Karol G x Shakira AND TQG', 0), ('Miguel AND Sure Thing', 105), ('RAYE Featuring 070 Shake AND Escapism', 3), ('Morgan Wallen AND One Thing At A Time', 110), ('Eslabon Armado X Peso Pluma AND Ella Baila Sola', 1), ('Drake & 21 Savage AND Rich Flex', 65), ('Kane Brown With Katelyn Brown AND Thank God', 0), ('Stephen Sanchez AND Until I Found You', 75), ('Jimin AND Set Me Free, Pt. 2', 7460), ('Beyonce AND Cuff It', 328), ('Luke Combs AND Going, Going, Gone', 19), ('Zach Bryan AND Something In The Orange', 24), ('Metro Boomin, Future & Chris Brown AND Superhero (Heroes & Villains)', 31), ('Lainey Wilson AND Heart Like A Truck', 11), ('SZA AND Snooze', 368), ("Carly Pearce AND What He Didn't Do", 20), ('Morgan Wallen AND Everything I Love', 12), ("Morgan Wallen AND Ain't That Some", 3), ('Drake & 21 Savage AND Spin Bout U', 29), ('Lady Gaga AND Bloody Mary', 361), ('JVKE AND Golden Hour', 204), ('HARDY Featuring Lainey Wilson AND Wait In The Truck', 0), ('SZA AND Shirt', 78), ('Luke Combs AND 5 Leaf Clover', 28), ('Morgan Wallen AND I Wrote The Book', 5), ('Nicki Minaj AND Red Ruby Da Sleeze', 270), ('Superstar Pride AND Painting Pictures', 15), ('Luke Combs AND Love You Anyway', 22), ('Fuerza Regida X Grupo Frontera AND Bebe Dame', 3), ('Morgan Wallen Featuring Eric Church AND Man Made A Bar', 0), ('SZA AND Nobody Gets Me', 129), ('Bizarrap & Shakira AND Bzrp Music Sessions, Vol. 53', 50), ('Morgan Wallen Featuring ERNEST AND Cowgirls', 0), ('Jordan Davis AND Next Thing You Know', 5), ('Lizzy McAlpine AND Ceilings', 63), ('Corey Kent AND Wild As Her', 8), ('Parker McCollum AND Handle On You', 7), ('Miley Cyrus AND River', 285), ('Ice Spice AND In Ha Mood', 132), ("Morgan Wallen AND '98 Braves", 16), ('Morgan Wallen AND Sunrise', 6), ('Lizzo Featuring SZA AND Special', 0), ('Lil Baby AND Freestyle', 53), ('The Kid LAROI AND Love Again', 62), ('Metro Boomin, Travis Scott & Young Thug AND Trance', 21), ('Hozier AND Eat Your Young', 195), ('Megan Moroney AND Tennessee Orange', 14), ('Sabrina Carpenter AND Nonsense', 142), ('Gabito Ballesteros, Peso Pluma & Natanael Cano AND AMG', 2), ('Yandel & Feid AND Yandel 150', 39), ('Peso Pluma AND Por Las Noches', 56), ('Peso Pluma X Natanael Cano AND PRC', 1), ('Lil Baby Featuring Fridayy AND Forever', 0), ('Lil Uzi Vert AND Watch This (ARIZONATEARS Pluggnb Remix)', 5), ('Zach Bryan Featuring Maggie Rogers AND Dawns', 0), ('Yng Lvcas x Peso Pluma AND La Bebe', 1), ('Carin Leon X Grupo Frontera AND Que Vuelvas', 5), ('Morgan Wallen AND Dying Man', 2), ('Morgan Wallen AND Whiskey Friends', 7), ('SZA AND Low', 197), ('Niall Horan AND Heaven', 168), ("Tyler Hubbard AND Dancin' In The Country", 4), ('Chino Pacas AND El Gordo Trae El Mando', 6), ('Tiesto Featuring Tate McRae AND 10:35', 0), ("Morgan Wallen AND Devil Don't Know", 1), ('Eladio Carrion & Bad Bunny AND Coco Chanel', 19), ('Coco Jones AND ICU', 491), ("Brett Young AND You Didn't", 12), ('Morgan Wallen AND Neon Star (Country Boy Lullaby)', 1), ('Cody Johnson AND Human', 5), ('Kali Uchis AND Moonlight', 194), ('Dierks Bentley AND Gold', 8), ('Morgan Wallen AND Born With A Beer In My Hand', 0), ('Melanie Martinez AND Death', 1060), ('Russ AND Nasty', 34), ('Miley Cyrus AND Jaded', 189), ('d4vd AND Here With Me', 89), ('Morgan Wallen AND Me + All Your Reasons', 5), ('Fifty Fifty AND Cupid', 2487)]
        #print(tweet_comp)

        # Create a Pandas DataFrame from the video data
        columns = ["Song_Artist-Title","Song_Tweets"]
        return pd.DataFrame(tweet_comp, columns=columns)


    # Sort songs
    def rank_tweets():
        ranked_df = Twitter.process_tweets.sort_values(by=['Song_Tweets'], ascending=False)
        ranked_df.reset_index(drop=True, inplace=True)
        return ranked_df
    def sorted_tweets():
        return Twitter.rank_tweets()

