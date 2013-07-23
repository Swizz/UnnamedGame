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
    'startword': u'jouer',
    'items': [
        # Armes blanches
        u'un couteau', u'une hache', u'un katana', u'une tronçoneuse',
        u'un secateur', u'une matraque', u'une machette', u'un tesson',
        u'une faucille', u'une beche', u'une pelle', 'un gourdin',
        # Armes à feu
        u'un 9mm', u'un sniper', u'un M16', u'un canon scié',
        u'un AK-47', u'une arbalète', u'un arc', u'une grenade',
        # Electronique
        u'un telephone', u'un ordinateur', u'une radio', u'un baladeur',
        u'un talkie-walkie', u'un laser', u'une lampe torche',
        u'une TV', 'des ecouteurs',
        # Divers
        u'un tournevis', u'une peluche', u'une conserve', u'un caddie',
        u'une chaise', u'un ballon', u'un oeuf', u'une guitare', u'une flute',
        u'un cd', u'des clous', u'un billet', u'un bonbon', u'une peluche',
        u'un ventilateur', u'un dictionnaire', u'une assiette', u'un coussin',
        u'une poubelle', u'une louche', u'une pagaie', u'un mouchoir',
        u'un chiwawa', u'un chat', u'une fourchette', u'un clavier'
    ],
    'sentences': [
        u'Des montagnes de cadavres inanimés pullulent.\n'
        u'Mais tous ne sont pas sans vie. D\'ailleurs quelques uns vous ont remarqué.',

        u'Vous entrez dans des toilettes publiques, et l\'odeur est insoutenable.\n'
        u'Sans crier gare, un zombie cul nu vous saute dessus.',
    ],

    # Elements du message final
    'message': u'%(sentence)s \n'
               'Objets : %(allowed_items)s',
    'linkers' : (u', ', u' et ')
}

language['fr'] = _FR
