

import json
import chardet
from collections import Counter


def encoding():
    with open(input('Введите имя файла (например newscy.json): '), 'rb') as f:
        data = f.read()
        enc_data = chardet.detect(data)
        data = data.decode(enc_data['encoding'])
        data = json.loads(data)
        text = ''

        for item in data['rss']['channel']['items']:
            text += ' ' + item['description']

    return text


def find_words(text):
    list_words = list()

    for word in text.split(' '):
        if len(word) > 6:
            list_words.append(word)

    count_words = Counter(list_words)
    sorted_words = sorted(dict(count_words).items(), key=lambda k: k[1], reverse=True)
    for i in sorted_words[:10]:
        print('Слово - {}\nКолличество повторов - {}\n'.format(i[0], i[1]))







find_words(encoding())
