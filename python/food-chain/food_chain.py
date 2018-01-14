def chain():
    know = "I know an old lady who swallowed a {}."
    swallowed = "She swallowed the {} to catch the {}."
    animals_remarks = (
        ('fly', "I don't know why she swallowed the fly. Perhaps she'll die."),
        ('spider', 'It wriggled and jiggled and tickled inside her.'),
        ('bird', 'How absurd to swallow a bird!'),
        ('cat', 'Imagine that, to swallow a cat!'),
        ('dog', 'What a hog, to swallow a dog!'),
        ('goat', 'Just opened her throat and swallowed a goat!'),
        ('cow', "I don't know how she swallowed a cow!"),
        ('horse', "She's dead, of course!"),
    )

    lyrics = []
    for ari, (animal, remark) in enumerate(animals_remarks):
        lyrics.append(know.format(animal))
        lyrics.append(remark)
        if 0 < ari < 7:
            for i in range(ari, 0, -1):
                catcher = animals_remarks[i][0]
                caught = animals_remarks[i - 1][0]
                if caught == 'spider':
                    caught += ' that wriggled and jiggled and tickled inside her'
                lyrics.append(swallowed.format(catcher, caught))
            lyrics.append(animals_remarks[0][1])
        lyrics.append('')

    return '\n'.join(lyrics).strip()