def rotate(text, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alow = [c for c in alphabet]
    aupp = [c for c in alphabet.upper()]
    cipher_dict = dict(zip(alow + aupp, alow[rot:] + alow[:rot] + aupp[rot:] + aupp[:rot]))
    return ''.join([cipher_dict[c] if c.isalpha() else c for c in text])
