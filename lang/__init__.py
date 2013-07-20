# -*- coding: utf8 -*-
''' A lot of things to manage language support '''

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

language = {}
from . import fr

def concat_items(lang, items_list):
    ''' Concatenate the items list in a right sentence '''
    linkers = language[lang]['linkers']
    
    items_sentence = ''
    items_number = len(items_list)

    for pos, item in enumerate(items_list):
        if(pos == items_number-1):
            items_sentence += linkers[1]
        elif(pos > 0):
            items_sentence += linkers[0]

        items_sentence += item

    return items_sentence

def write_message(lang, sentence, items_list):
    ''' Write the sended message '''
    base_message = language[lang]['message']

    return base_message % \
           { 'sentence': sentence, 
            'allowed_items': concat_items(lang, items_list)}
