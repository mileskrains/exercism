import random
import string


class Cipher():
    def __init__(self, key=None):
        if key == None:
            self.key = ''.join(random.choices(string.ascii_lowercase, k=100))
        else:
            if key == ''.join([c.lower() for c in key if c.isalpha()]):
                self.key = key
            else:
                raise ValueError
    
    def _enc(self, t, k):
        eo = ord(t)+ord(k)-97
        if eo > 122:
            eo -= 26
        return(chr(eo))

    def _dec(self, t, k):
        do = ord(t)-ord(k)+97
        if do < 97:
            do += 26
        return(chr(do))
    
    def _confirm_keylength(self, num):
        while len(self.key) < num:
            self.key += self.key
    
    def encode(self, text):
        text = ''.join([c.lower() for c in text if c.isalpha()])
        self._confirm_keylength(len(text))
        return ''.join([self._enc(t, k) for t, k in zip(text, self.key)])

    def decode(self, text):
        self._confirm_keylength(len(text))
        return ''.join([self._dec(t, k) for t, k in zip(text, self.key)])

    
class Caesar(Cipher):
    def __init__(self):
        super().__init__(key='d')
