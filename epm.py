import tweepy

def get_api(cfg)P
    auth = tweepy.OAuthHandler(cfg['consumer_key'],cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def main():

    cfg = {
        "consumer_key": "v4ixoHp4aD5eEul3pPXKsgmK",
        "consumer_secret": "5PH2rRCQVAsr4E8VtDCJyzeMVRi1rop1e9g9TdfZ3TO43oSXFY",
	"access_token": "4746180908-NhW50ATNFC9wBxNHDefTUXJNcGVkWdzcVLTWltN",
        "access_token_secret": "rzDLPeggfeXyfMrSodpaMfSHfJ3HF3OjTAZKxeTi4G64M"
    }

    api = get_api(cfg)
    tweet = "The emojipasta maker is on"
    status = api.update_status(status=tweet)

if __name__ == "__main__":
    main()
