from random import random
import win32clipboard
import re
# this should be switched up to separate files and such

TRANSLATE = {
    'ф': chr(1060), 'Ф': chr(1092),
    'ё': 'ø', 'Ё': 'Ø',
    'З': chr(1047), 'з': chr(1079),
    'е': 'ѣ', 'Е': 'Ѣ',
    'Ф': 'Ѳ', 'ф': 'ѳ',
    # 'о': 'ѡ', 'О': 'Ѡ',
    'з': chr(1109), 'З': chr(1029),
    'Э': chr(1028), 'э': chr(1108),
    'Ы': 'Ѵ', 'ы': 'ѵ',
}

WORDS = {
    'писал': 'ѱалѣ', 'писать': 'ѱатѣ', 'пишу': 'ѱишу'
}

VOWELS = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
CONSONANTS = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']

BEFORE_HARD_MARK = ['б', 'в', 'г', 'д', 'ж', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш']


def replace_keep_case(word, replacement, text):
    def func(match):
        g = match.group()
        if g.islower(): return replacement.lower()
        if g.istitle(): return replacement.title()
        if g.isupper(): return replacement.upper()
        return replacement
    return re.sub(word, func, text, flags=re.I)

def mush(data):
    for word in WORDS:
        # test = re.compile(f"(?i)(?=((?:\W|\n|^){word}(?:\W|\n|$)))", flags=re.MULTILINE)
        data = replace_keep_case(word, WORDS[word], data)
    new_data = list()
    for i in range(data.__len__()):
        new_data.append(data[i])
        if (i == data.__len__()-1 or data[i+1] in [' ', ',', '.', ';', '!', '?']) and data[i] in BEFORE_HARD_MARK and (random()>0.55):
            new_data.append('Ѣ'.lower())
    # add here differentiation between "мир" as in world and as in peace and change up accordingly.
    data = ''.join(new_data)
    # proper i-s and other word-by-word change
    new_data = list()
    for word in data.split(' '):
        for i in range(word.__len__()-1):
            if word[i] in ['и', 'И'] and i < word.__len__() - 1:
                if word[i + 1].lower() in ['й', ] + VOWELS:
                    word = word[0:i] + (chr(1031) if word[i].isupper() else chr(1111)) + word[i + 1:]
        new_data.append(word)
    data = ' '.join(new_data)
    for char in TRANSLATE:
        data = data.replace(char, TRANSLATE[char])
    # Мироздание требует возмездия за такие выкрутасы
    return data

win32clipboard.OpenClipboard()
cdata = win32clipboard.GetClipboardData()#.encode('utf-8')
cdata = mush(cdata)
win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, cdata)
win32clipboard.CloseClipboard()