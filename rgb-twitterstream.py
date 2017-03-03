#! python

import time
from sys import exit, argv

try:
    from tweepy import Stream, OAuthHandler
    from tweepy.streaming import StreamListener
except ImportError:
    exit("This script requires the tweepy module\nInstall with: sudo pip instal$

from blinkt import set_pixel, show, set_all, clear, set_brightness

ckey = '9p7mvsfa0tve6ZYgLd0foljOB' # Consumer key
csecret = 'RIMiCYfnodbGKzpb5nXyhiHft9EHp8ZsPeUfJJmNe2vSIIJpLJ' # Consumer secret
atoken = '74130610-NkuJz28gbtJZ72ZBqJddFy4eGig4fEU9Ns6zBV9D0' # Access token
asecret = 'TQmkaw2IYfMV1ep9dVUz0EhneYoc0eu6q13hvo4ibVk9l' # Access secret

class listener(StreamListener):

    def on_status(self, status):
        for k,v in hash_color_dict.items():
            if k in status.text:
                set_brightness(1)
                blink_blinkt(v[0], v[1], v[2])
                return True

    def on_error(self, status):
        print status

def blink_blinkt(r,g,b):
    set_all(r, g, b)
    show()
    time.sleep(0.1)
    clear()
    show()

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterstream = Stream(auth, listener())

hash_color_dict={
                    "#infosec":(255,0,0),
                    "#python":(0,0,255),
                    "#fun":(0,255,0)
                    }

twitterstream.filter(track=[hashtag for hashtag in hash_color_dict.keys()])
