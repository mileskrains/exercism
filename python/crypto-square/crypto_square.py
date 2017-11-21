import math


def encode(plain_text):
    pt_norm = [c for c in plain_text.lower() if c.isalnum()]
    pt_char_ct = len(pt_norm)
    if pt_char_ct < 3:
        return ''.join(pt_norm)
    c = r = int(round(math.sqrt(pt_char_ct),0))
    if r**2 < pt_char_ct:
        c += 1
        
    ct = ''
    for x in range(c):
        for y in range(r):
            pos = x+y*c
            if pos < pt_char_ct:
                ct += pt_norm[pos]
            else:
                ct += ' '
            if pos >= c * (r-1):
                ct += ' '
    return ct[:r*c+c-1]
