# -*- coding: utf8 -*-
''' The FR language support dictionary '''

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

from lang import language

_FR = {
    'startword': 'jouer',
    'items': [
        # Armes blanches
        'un couteau', 'une hache', 'un katana', 'une tronçoneuse',
        # Armes à feu
        'un 9mm', 'un sniper', 'un M16',
        # Electronique
        'un telephone', 'un ordinateur', 'une radio',
        # Divers
        'un tournevis', 'une peluche', 'une conserve',
    ],
    'sentences': [
        'Face à un glacier, bien gardé, votre seul désire est d\' y entrer',
    ],

    # Elements du message final
    'message': '%(sentence)s \n'
               'Objets : %(allowed_items)s',
    'linkers' : (', ', ' et ')
}

language['fr'] = _FR
