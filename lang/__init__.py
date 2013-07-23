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
    
    items_sentence = u''
    items_number = len(items_list)

    if(len(items_list) > 1):
        for pos, item in enumerate(items_list):
            if(pos == items_number-1):
                items_sentence += linkers[1]
            elif(pos > 0):
                items_sentence += linkers[0]
            items_sentence += item
    else:
        items_sentence += items_list[0]

    return items_sentence

def write_message(lang, sentence, items_list):
    ''' Write the sended message '''
    base_message = language[lang]['message']

    items_sentence = concat_items(lang, items_list)

    return base_message % \
           { 'sentence': sentence, 
             'allowed_items': items_sentence}

def get_language(string, key=None):
    ''' Get the language of a string
        
        You can specify an optional key '''

    for lang, dic in language.items():
        if(key is None):
            for key, values in dic.items():
                if string in values:
                    return lang
        else:
            if string in dic[key]:
                return lang

    return None

def check_sentence(lang=None):
    ''' Check the length of all sentence in a
        specicific language, or not. '''

    MAX_LENGTH = 123 #max pseudo lentght is 15
                     #max tweet length is 140

    if lang is None :
        for lang, dic in language.items():
            for sentence in dic['sentences']:
                if len(sentence) > MAX_LENGTH:
                    print '%s: %s >>> %d' % (lang, sentence, len(sentence))
    else:
        for sentence in language[lang]['sentences']:
            if len(sentence) > MAX_LENGTH:
                print '%s: %s >>> %d' % (lang, sentence, len(sentence))
