def decode(encoding):
    digits = ''
    decoding = ''
    def _count_int(digits):
        return 1 if digits == '' else int(digits)
    
    for char in encoding:
        if char in '1234567890':
            digits = digits + char
        else:
            decoding = decoding + _count_int(digits) * char
            digits = ''
    return decoding


def encode(plaintext):
    prior = ''
    count = 1
    encoding = ''
    def _count_string(ct):
        return str(ct) if ct > 1 else ''
    
    for char in plaintext:
        if char == prior:
            count += 1
        else:
            encoding = encoding + _count_string(count) + prior
            count = 1
        prior = char
    encoding = encoding + _count_string(count) + prior
    return encoding
