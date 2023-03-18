import tweepy
import time

# Authenticate with Twitter API using OAuthHandler and access token
auth = tweepy.OAuthHandler('consumer_key',
                           'consumer_secret')
auth.set_access_token('access_token',
                      'access_token_secret')

# Initialize API object with authentication credentials
api = tweepy.API(auth, wait_on_rate_limit=True)

# Define search parameters
mixed = 'mixed' # Type of results to search for (mixed, recent, popular)
recent = 'recent'
popular = 'popular'

search = 'python','JavaScript' # Search terms
count = 50 # Number of tweets to search for
screen_name = "Avinash" # Twitter screen name to reply to
lang = 'en' # Language of tweets to search for
status = 'Hello Isekai' # Status message to reply with
filename = "acv.png" # Filename of image to attach to reply

# Search for tweets that match the search criteria
response = api.search_tweets(q=search, count=count, result_type=mixed, lang=lang,) 

# Iterate over each tweet in the response list and reply to them
for tweet in response:
   try:  
     # Print message indicating that tweet has been liked
     print('Tweet Liked')

     # Reply to the tweet with a status message and attached image
     api.update_status(status = status, in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
     api.update_status_with_media(filename= filename, status = status, in_reply_to_status_id = tweet.id)

     # Favorite the tweet
     tweet.favorite()

     # Wait for 25 seconds before moving to the next tweet
     time.sleep(25)

   # Catch and print any Forbidden errors that may occur
   except tweepy.errors.Forbidden as e: 
         print(e)

   # Break out of the loop if a StopIteration error occurs
   except StopIteration:
         break

# Run the code by executing this command in the terminal
# python bot1.py
