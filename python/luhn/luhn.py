class Luhn(object):
    def __init__(self, cand):
        self.cand = cand
    
    def is_valid(self):
        sval = self.cand.replace(' ', '')
        if not sval.isdigit() or len(sval)<2:
            return False
        sval = [int(c) for c in reversed(sval)]
        return sum(sval[::2] + [2*n if n<5 else 2*n-9 for n in sval[1::2]]) % 10 == 0
