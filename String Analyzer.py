# Project : String Analyzer/Checker
# Importing required libraries
from gingerit.gingerit import GingerIt
from PyDictionary import PyDictionary


class Stringanalyzer:
    def __init__(self, string):
        self.ipstring = string

# Function to correct the input string.

    def check(self):
        p = GingerIt()
        res = p.parse(self.ipstring)['result']
        if '-' in res:
            res.replace('-', ' ')
        return res.capitalize()

# Function to get word count of input string.
    def word_count(self):
        p = GingerIt()
        res = p.parse(self.ipstring)['result']
        all_words = res.casefold().split()
        words = {}
        # Removing special characters (if any)
        for i in all_words:
            if i.find('.') != -1:
                all_words[all_words.index(i)] = i.replace('.', '')
            elif i.find('!') != -1:
                all_words[all_words.index(i)] = i.replace('!', '')
            elif i.find(',') != -1:
                all_words[all_words.index(i)] = i.replace(',', '')
            elif i.find('/') != -1:
                all_words[all_words.index(i)] = i.replace('/', '')
            elif i.find('?') != -1:
                all_words[all_words.index(i)] = i.replace('?', '')
            elif i.find(')') != -1:
                all_words[all_words.index(i)] = i.replace(')', '')
            elif i.find('(') != -1:
                all_words[all_words.index(i)] = i.replace('(', '')
            elif i.find(':') != -1:
                all_words[all_words.index(i)] = i.replace(':', '')
            elif i.find('-') != -1:
                all_words[all_words.index(i)] = i.replace('-', '')
            else:
                continue
        # Creating a dictionary with key = word and value = occurrence of that word
        for i in all_words:
            if i in words:
                words[i] += 1
            else:
                words[i] = 1
        return words, len(all_words)

# Function to get definition of all the words in the string.
    def get_definition(self):
        p = GingerIt()
        res = p.parse(self.ipstring)['result']
        # all_words = res.split()
        all_words = self.word_count()[0]
        dictionary = PyDictionary(all_words)
        for word in all_words:
            print(word + ':' + str(dictionary.meaning(word, disable_errors=True)))


# Function to calculate number of letters in a string.
    def no_of_letters(self):
        let = 0
        for i in range(len(self.ipstring)):
            unic = ord(self.ipstring.lower()[i])
            if 97 <= unic <= 122:
                let += 1
        return let

# Function to calculate number of digits in a string.
    def no_of_digits(self):
        dig = 0
        for i in range(len(self.ipstring)):
            unic = ord(self.ipstring.lower()[i])
            if 48 <= unic <= 57:
                dig += 1
        return dig


x = Stringanalyzer(input())
print(x.check())
print(x.word_count())
x.get_definition()
print('No. of letters : ', x.no_of_letters())
print('No. of digits : ', x.no_of_digits())

