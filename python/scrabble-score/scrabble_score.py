def score(word):
    def add_score(chars, score):
        for c in chars:
            letter_scores[c] = score
    letter_scores = {c:1 for c in 'aeioulnrst'}
    add_score('dg', 2)
    add_score('bcmp', 3)
    add_score('fhvwy', 4)
    add_score('k', 5)
    add_score('jx', 8)
    add_score('qz', 10)
    return sum([letter_scores[c] for c in word.lower()])
