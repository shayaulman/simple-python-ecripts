import re

letters = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 20, 'l': 30, 'm': 40, 'n': 50, 'o': 60, 'p': 70, 'q': 80, 'r': 90, 's': 100, 't': 200, 'u': 100, 'v': 300, 'w': 400, 'x': 500, 'y': 600, 'z':700 }

def get_input():
    user_input = raw_input('Please enter a word...').replace(u' ', '')
    if not re.match('[a-zA-Z]', user_input):
        print "Pllease enter only English Characters!"
        get_input()
    return user_input

def gimatriya(word):
    gimatriya = 0
    for letter in word:
        gimatriya += letters[letter]
    return gimatriya

print "The result is: " + str(gimatriya(get_input()))
