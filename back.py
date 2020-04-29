from difflib import get_close_matches as g_c_m
import json_data

data = json_data.data

answers = ['yes', 'yeah', 'y', 'yep']


def greetings(first_time):
    """Welcome message for user"""
    if first_time:
        print("Hello! I will help you to find the meaning of the words :)")
    else:
        print("Let's try again!")
    u_word = input("Please, enter your word: ")
    return u_word


def translate(word):
    """Word search in json's dic"""
    if word.lower() in data:
        return data[word.lower()]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data:
        return data[word.upper()]
    elif not g_c_m(word, data.keys()):
        return no_word(word)
    else:
        return maybe_mistake(word)


def no_word(u_word):
    """No-word-in-dic message"""
    return "I don't know the '{}' word :(".format(u_word,)


def maybe_mistake(word):
    """Trying to find similar words"""
    best_word = g_c_m(word.lower(), data.keys())[0]
    answer = input('Did u mean "{}" instead? '
                   'Enter "Yes" if yes.\n'.format(best_word))
    if not g_c_m(answer.lower(), answers):
        return no_word(word)
    else:
        return data[best_word]
