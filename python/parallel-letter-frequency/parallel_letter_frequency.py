import concurrent.futures
from collections import Counter
from functools import reduce


def to_letter_counts(text):
    return Counter([c for c in text.lower() if c.isalpha()])

def calculate(text_input):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        counters = executor.map(to_letter_counts, text_input)
    all_count = reduce(lambda d1, d2: d1 + d2, counters)
    return dict(all_count)
