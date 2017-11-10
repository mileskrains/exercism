def is_pangram(sentence):
    alphas = set('abcdefghijklmnopqrstuvwxyz')
    return alphas.issubset(set(sentence.lower()))
