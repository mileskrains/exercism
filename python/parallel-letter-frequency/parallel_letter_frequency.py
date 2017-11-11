import concurrent.futures
from collections import Counter
from functools import reduce
from operator import add


def to_letter_counts(text):
    return Counter([c for c in text.lower() if c.isalpha()])

def calculate(text_input):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        counters = executor.map(to_letter_counts, text_input)
    all_count = reduce(add, counters)
    return dict(all_count)

