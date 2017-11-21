def translate_word(word):
    vowels = 'aeiouy'
    start = ''
    rest = word
    while (rest[0] not in vowels or
           (start.endswith('q') and rest[0] == 'u') or
           (start == '' and rest[0] == 'y' and rest[1] in vowels)):
        start += rest[0]
        rest = rest[1:]
    if rest == 'ay':
        start = ''
        rest = word
    return rest + start + 'ay'

def translate(text):
    return ' '.join([translate_word(w) for w in text.split()])
