from collections import Counter
import re


def word_count(phrase):
    phrase = re.sub('[^0-9a-zA-Z\']+', ' ', phrase.lower())
    phrase = ' '.join([w.strip("'") for w in phrase.split()])
    return dict(Counter(phrase.split()))

