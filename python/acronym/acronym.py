def abbreviate(words):
    take = True
    acronym = ''
    for c in words:
        if c.isalpha():
            if take:
                acronym += c
                take = False
        else:
            take = True
    return acronym.upper()
