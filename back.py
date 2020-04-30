from difflib import get_close_matches as g_c_m, SequenceMatcher
import json_data

data = json_data.data

answers = ['yes', 'yeah', 'y', 'yep']


def greetings(first_time):
    """Welcome message for user"""
    if first_time:
        print("Hello! I will help you to find the meaning of the words :)")
    else:
        print("Let's try again! \nOr type 'Exit() to close the session\n")
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
    else:
        return sequences(word)


def sequences(word):
    """Trying to find similar words in json"""
    dic_seq = {}
    lower_gcm = g_c_m(word.lower(), data.keys())
    upper_gcm = g_c_m(word.upper(), data.keys())
    cap_gcm = g_c_m(word.capitalize(), data.keys())
    for i in [lower_gcm, upper_gcm, cap_gcm]:
        if i:
            if SequenceMatcher(None, word, i[0]).ratio() > 0:
                dic_seq[i[0]] = SequenceMatcher(None, word, i[0]).ratio()
    if dic_seq:
        best = max(dic_seq, key=dic_seq.get)
        return maybe_mistake(best, word)
    else:
        return no_word(word)


def no_word(word):
    """No-word-in-dic message"""
    return "I don't know the '{}' word :(".format(word,)


def maybe_mistake(best, word):
    """Asking for a similar word"""
    answer = input('Did u mean "{}" instead? '
                   'Enter "Yes" if yes.\n'.format(best))
    if not g_c_m(answer.lower(), answers):
        return no_word(word)
    else:
        return data[best]
