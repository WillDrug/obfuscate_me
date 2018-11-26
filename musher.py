import random
import re
import pymorphy2

THRESHOLD = 0.7
TRANSLATE = {  # not using utf-8 codes to know which chars already used
    'гь': ['Ꙉ'],
    'жь': ['ʒ'],
    'пь': ['ѱ'],
    'пи': ['ѱ'],
    'оу': ['ꙋ'],
    'Ф': ['ф', 'ѳ'],
    'я': ['ѧ'],
    'ё': ['ø'],
    'з': ['з', 'ѕ', 'ꙁ'],  # ß somehow does not pass upper() well =\ don't want to rewrite everything because of it
    'и': ['ї'],
    'е': ['ѣ'],
    'ф': ['ѳ'],
    'о': ['ѡ'],
    'э': ['є'],
    'у': ['ѫ'],
    'г': ['ȝ', 'ћ'],
    'д': ['ⰼ'],
}
VOWELS = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']
CONSONANTS = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
BEFORE_HARD_MARK = ['б', 'в', 'г', 'д', 'ж', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш']
dicts = pymorphy2.analyzer.MorphAnalyzer()

def normalize_with_threshold(threshold):
    def normalize_regex_parmed(matchobj):
        return normalize(matchobj.group(), threshold=threshold)
    return normalize_regex_parmed

def normalize_regex(match):
    return normalize(match.group())

def normalize(data, threshold = None):
    if threshold is None:
        threshold = THRESHOLD
    # normalize by morpher
    # TODO: normalize by levenstein distance (may be collect most used words) or use an online dictionary service
    # or google api or something.
    replacement = dicts.parse(data)[0].word
    if replacement.__len__() == data.__len__():
        repl = [q for q in replacement]
        matl = [q for q in data]
        if repl.__len__() == matl.__len__():
            for i in range(matl.__len__()):
                if matl[i].islower():
                    repl[i] = repl[i].lower()
                else:
                    repl[i] = repl[i].upper()
            replacement = ''.join(repl)

    # now how about some hard marks... not everywhere, of course.
    if replacement[-1] in BEFORE_HARD_MARK and random.random() > threshold:
        replacement = replacement + ('Ҍ' if replacement[-1].isupper() else 'ҍ')
    # now let's choose one substitute for each letter available to change up
    letters = {q: TRANSLATE[q][random.randint(0, TRANSLATE[q].__len__()-1)] for q in TRANSLATE}
    for letter in letters:
        if random.random() > threshold:
            for i in re.finditer(letter, replacement.lower()):
                found = replacement[i.span()[0]:i.span()[1]]
                if found.isupper():
                    replacement = replacement[0:i.span()[0]] + letters[letter].upper() + replacement[i.span()[1]:]
                elif found.islower():
                    replacement = replacement[0:i.span()[0]] + letters[letter].lower() + replacement[i.span()[1]:]
                elif found.istitle():
                    replacement = replacement[0:i.span()[0]] + letters[letter].title() + replacement[i.span()[1]:]
                else:
                    replacement = replacement[0:i.span()[0]] + letters[letter] + replacement[i.span()[1]:]
    return replacement


def mush(data, single=False, threshold=None):
    if single:
        return normalize(data, threshold=threshold)
    else:
        test = re.compile("\w+")  #each word
        if threshold is not None:
            data = re.sub(test, normalize_with_threshold(threshold), data)
        else:
            data = re.sub(test, normalize_regex, data)
        # print(data)
        return data

if __name__ == '__main__':
    print(mush('Съешь еще этих, СЪЕШЬ! мягких)) ЕщЕ *французских* :( булок да... да выпей чаю, зелибоба? Гьрь', threshold=-1))
