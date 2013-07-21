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
from lang import get_language
from core import Core
import json
import re

Ukey = 'censored'
Usecret = 'censored'

Akey = 'censored'
Asecret = 'censored'

BotName = 'censored'

class Streamer(StreamListener):
    ''' A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    '''

    def __init__(self, crawler):
        self.line = 0
        self.crawler = crawler

    def on_data(self, data):
        data = json.loads(data)


        if(self.line>0):
            if('in_reply_to_screen_name' in data):
                if(data['in_reply_to_screen_name'] == self.crawler.name):
                    self.crawler.on_request(data['text'], data['user']['screen_name'])

        self.line+=1
        return True

    def on_error(self, status):
        print u'Erreur :::', status
        return True



class Crawler():
    ''' The global crawler manager '''

    def __init__(self, name):
        self.name = name
        self.regexp = re.compile(r'@%s\s+' % (self.name),
                                 re.IGNORECASE)

        self._start_stream()


    def _auth(self):
        self.auth = OAuthHandler(Ukey, Usecret)
        self.auth.set_access_token(Akey, Asecret)

        self.api = API(self.auth)

    def _start_stream(self):
        self.listener = Streamer(self)

        self._auth()

        self.stream = Stream(self.auth, self.listener)
        self.stream.userstream()

    def on_request(self, text, author):
        text = re.sub(self.regexp, '', text)
        text = re.sub(r'\s+$', '', text)

        lang = get_language(text, key='startword')
        core = Core(lang)

        self.send_message(core.send_message(), author)

    def send_message(self, text, target=None):
        if(target is not None):
            text = u'@%s %s' % (target, text)

        self.api.update_status(text)

if __name__ == '__main__':
    this = Crawler(BotName)
