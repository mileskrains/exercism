def hey(phrase):
    phrase = phrase.strip()
    if phrase == '':
        return 'Fine. Be that way!'
    if phrase.isupper():
        return 'Whoa, chill out!'
    elif phrase[-1] == '?':
        return 'Sure.'
    else:
        return 'Whatever.'

