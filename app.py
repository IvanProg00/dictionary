from json import load
from pathlib import Path
from os import path
from difflib import get_close_matches

root = Path(__file__).resolve().parent
dict_file = open(path.join(root, 'dictionary.json'), 'r')
dict_json = load(dict_file)


def not_found():
    print('Word not found.')

def ask_word():
    word = ''
    while not word:
        word = input('Input a word: ').strip()
        if not word:
            print('You must enter something.')
    search_word(word)


def search_word(word):
    if word in dict_json.keys():
        print(dict_json[word])
    else:
        words_could_mean = get_close_matches(word, dict_json.keys(), n=1)
        if len(words_could_mean) > 0:
            word_could_mean = words_could_mean[0]
            user_say = input(f'Did you mean "{word_could_mean}" print Y\\n: ')
            if user_say.lower().strip() == 'y':
                search_word(word_could_mean)
            else:
                not_found()
        else:
            not_found()



print('Dictionary')
ask_word()
