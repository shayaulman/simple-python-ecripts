# -*- coding: utf-8 -*-
import re

letters = { u'א': 1, u'ב': 2, u'ג': 3, u'ד': 4, u'ה': 5, u'ו': 6, u'ז': 7, u'ח': 8, u'ט': 9, u'י': 10, u'כ': 20, u'ך': 20, u'ל': 30, u'מ': 40, u'ם': 40, u'נ': 50, u'ן': 50, u'ס': 60, u'ע': 70, u'פ': 80, u'ף': 80, u'צ': 90, u'ץ': 90, u'ק': 100, u'ר': 200, u'ש': 300, u'ת': 400 }

def get_input():
    user_input = raw_input('נא הכנס מילה לחישוב!').decode("utf-8").replace(u' ', '')
    if re.match('[a-zA-Z]', user_input):
        print "נא להכניס רק מילים בעברית!"
        get_input()
    return user_input

def gimatriya(word):
    gimatriya = 0
    for letter in word:
        gimatriya += letters[letter]
    return gimatriya

print gimatriya(get_input())


    