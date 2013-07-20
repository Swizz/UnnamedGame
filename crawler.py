# -*- coding: utf8 -*-
''' How to manage I/O '''

'''
Copyright (c) 2013 GERODEL Quentin (aka Swizz540)

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
from tweepy.streaming import Stream, StreamListener
from tweepy import OAuthHandler, API
import json

Ukey = 'censored' 
Usecret = 'censored' 

Akey = 'censored' 
Asecret = 'censored' 


class Crawler(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """

    def __init__(self):
        self.line = 0

    def on_data(self, data):
        data = json.loads(data)


        if(self.line>0 and data["in_reply_to_screen_name"] == "Swizz540"):
            print data["user"]["name"], "[" + data["created_at"] + "]"
            print data["text"]

        self.line+=1
        return True

    def on_error(self, status):
        print "Erreur :::", status
        return True

if __name__ == '__main__':
    l = Crawler()
    auth = OAuthHandler(Ukey, Usecret)
    auth.set_access_token(Akey, Asecret)

    api = API(auth)
    print api.me().name

    stream = Stream(auth, l)
    stream.userstream()
