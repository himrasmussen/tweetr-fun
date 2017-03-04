#!/usr/bin/env python3

import time
from sys import exit, argv

try:
    from tweepy import Stream, OAuthHandler
    from tweepy.streaming import StreamListener
except ImportError:
    exit("This script requires the tweepy module\nInstall with: sudo pip install requests")

from blinkt import set_pixel, show, set_all, clear, set_brightness

ckey = '9p7mvsfa0tve6ZYgLd0foljOB' # Consumer key
csecret = 'RIMiCYfnodbGKzpb5nXyhiHft9EHp8ZsPeUfJJmNe2vSIIJpLJ' # Consumer secret
atoken = '74130610-NkuJz28gbtJZ72ZBqJddFy4eGig4fEU9Ns6zBV9D0' # Access token
asecret = 'TQmkaw2IYfMV1ep9dVUz0EhneYoc0eu6q13hvo4ibVk9l' # Access secret

class listener(StreamListener):

    def on_status(self, status):
        common_hashtags = set([hash for hash in status.text.lower().split() if "#" in hash]) & set(hash_color_dict.keys())
        if len(common_hashtags) == 0:
            pass
        elif len(common_hashtags) > 1:
            color = mix_colors(*[hash_color_dict[hashtag] for hashtag in common_hashtags])
            blink_blinkt(color)
            #print(color)
        else:
            blink_blinkt(hash_color_dict[''.join(common_hashtags)])
            #print(hash_color_dict[''.join(common_hashtags)])
        return True

    def on_error(self, status):
        print (status)

def blink_blinkt(rgb_tuple):
    set_all(*rgb_tuple)
    set_brightness(0.05)  
    show()
    time.sleep(0.2)
    clear()
    show()

def mix_colors(*rgb_tuples):
    new_colors = []
    for i in range(3):
        new_colors.append(sum([rgb[i] for rgb in rgb_tuples]) / len(rgb_tuples))
    return tuple(new_colors)



auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterstream = Stream(auth, listener())

hash_color_dict={
                    "#infosec":(255,0,255),
                    "#python":(255,255)
                    }

twitterstream.filter(track=[hashtag for hashtag in hash_color_dict.keys()])

