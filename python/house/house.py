def verse(vn):
    lines = (('house that Jack built.', ''),
             ('malt', 'lay in'),
             ('rat', 'ate'),
             ('cat', 'killed'),
             ('dog', 'worried'),
             ('cow with the crumpled horn', 'tossed'),
             ('maiden all forlorn', 'milked'),
             ('man all tattered and torn', 'kissed'),
             ('priest all shaven and shorn', 'married'),
             ('rooster that crowed in the morn', 'woke'),
             ('farmer sowing his corn', 'kept'),
             ('horse and the hound and the horn', 'belonged to'))
    verse = 'This is'
    for n in range(vn, -1 , -1):
        noun, verb = lines[n]
        verse += f' the {noun}'
        verse += f'\nthat {verb}' if verb else '\n'
    return verse.strip()


def rhyme():
    return '\n\n'.join([verse(n) for n in range(12)])
