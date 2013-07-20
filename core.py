# -*- coding: utf8 -*-
''' Crawler's core '''

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

from random import sample, randint, choice
from string import hexdigits
from lang import write_message, language

class Core:
    ''' A simple core uses in multithread mode '''

    def __init__(self, lang):
        ''' Set the uuid and language of this core '''
        self.uuid = '%s_%s' % (lang.upper(), ''.join(sample(hexdigits, 13)))
        self.lang = lang

    def _get_items(self):
        ''' Get the usable item list '''
        available_items = language[self.lang]['items']

        items_number = randint(1,3)
        allowed_item = sample(available_items, items_number)

        return items_number, allowed_item

    def _get_sentence(self):
        ''' Get the target sentence '''
        available_sentence = language[self.lang]['sentences']

        final_sentence = choice(available_sentence)

        return final_sentence

    def send_message(self):
        ''' Return the sended message '''

        sentence = self._get_sentence()
        items_number, items_list= self._get_items()

        return write_message(self.lang, sentence, items_list)


#Main use
if __name__ == '__main__':
    this = Core('fr')
    print this.send_message()
