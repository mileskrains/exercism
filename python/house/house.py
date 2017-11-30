def verse(vn):
    lines = (('the house that Jack built.', ''),
             ('the malt', 'lay in'),
             ('the rat', 'ate'),
             ('the cat', 'killed'),
             ('the dog', 'worried'),
             ('the cow with the crumpled horn', 'tossed'),
             ('the maiden all forlorn', 'milked'),
             ('the man all tattered and torn', 'kissed'),
             ('the priest all shaven and shorn', 'married'),
             ('the rooster that crowed in the morn', 'woke'),
             ('the farmer sowing his corn', 'kept'),
             ('the horse and the hound and the horn', 'belonged to'))
    verse = 'This is '
    for n in range(vn, -1 , -1):
        noun, verb = lines[n]
        verse += noun
        verse += f'\nthat {verb} ' if verb else '\n'
    return verse.strip()


def rhyme():
    return '\n\n'.join([verse(n) for n in range(12)])
