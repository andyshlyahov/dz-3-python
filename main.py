import sys
from random import choice

EOS = ['.', '?', '!']

def build_dict(words):
    dict = {}
    for i, word in enumerate(words):
        try:
            first, second, third = words[i], words[i+1], words[i+2]
        except IndexError:
            break
        key = (first, second)
        if key not in dict:
            dict[key] = []
        dict[key].append(third)

    return dict


def generate_sentence(dict):
    list = [key for key in dict.keys() if key[0][0].isupper()]
    key = choice(list)

    list = []
    first, second = key
    list.append(first)
    list.append(second)
    while True:
        third = choice(dict[key])
        list.append(third)
        if third[-1] in EOS:
            break
        key = (second, third)
        first, second = key

    return ' '.join(list)


def main():
    file_corpus = open("corpus.txt", 'r')
    text = file_corpus.read()
    words = text.split()
    dictionary = build_dict(words)
    file_dict = open("dictionary.txt", 'w')
    for key in dictionary.keys():
        file_dict.write(str(key) + " : " +str(dictionary[key]) + '\n')
    file_text = open("text.txt", 'w')
    for count in range(1000):
        sent = generate_sentence(dictionary)
        if count % 10 != 0:
            file_text.write(sent + ' ')
        else:
            file_text.write(sent + '\n')


if __name__ == "__main__":
    main()
