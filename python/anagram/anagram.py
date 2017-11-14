def detect_anagrams(word, candidates):
    dorw = ''.join(sorted(word.lower()))
    return [c for c in candidates if (word.lower()!=c.lower() and ''.join(sorted(c.lower()))==dorw)]
