from bluetooth import *
import tweepy

#Consumer keys and access tokens, used for OAuth
consumer_key = 'HiQxJbiWG8CNrKt4ShYpSg'
consumer_secret = 'Yf4JMTraHN3jZxS3UgLUKO85tuEfpaniF0jWKuaw'
access_token = '16225523-dkewCCHNGH7F02ya09VxLIqWwZBojWm5moRTrwiV0'
access_token_secret = 'mbDYEwZJiM7c9nr8K6EN9bNYqmpbarCwXHOcqRaEIA'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

#api.update_status("test")











print("Scanning for near by devieces")

nearby_devices = discover_devices(lookup_names = True)



print (f"Found {len(nearby_devices)} devies" )

for  addr, name in nearby_devices:
     print (f'{addr} {name}')
     
     if name == 'Hedwig':
        api.update_status("I am home")
         
         
         
