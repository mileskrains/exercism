def encode(plain_text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    digits = '1234567890'
    code_dict = dict(zip(alphabet+digits, alphabet[::-1]+digits))
    cipher_text = ''.join([code_dict[c] for c in plain_text.lower() if c.isalnum()])
    sep_cipher_text = ''
    while cipher_text:
        sep_cipher_text += cipher_text[:5] + ' '
        cipher_text = cipher_text[5:]
    return sep_cipher_text.strip()


def decode(ciphered_text):
    sep_plain_text = encode(ciphered_text)
    return sep_plain_text.replace(' ', '')
