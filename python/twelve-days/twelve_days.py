def verse(day_number):
    days = ('twelfth eleventh tenth ninth eighth seventh '
            'sixth fifth fourth third second first').split()
    gifts = ['twelve Drummers Drumming, ',
             'eleven Pipers Piping, ',
             'ten Lords-a-Leaping, ',
             'nine Ladies Dancing, ',
             'eight Maids-a-Milking, ',
             'seven Swans-a-Swimming, ',
             'six Geese-a-Laying, ',
             'five Gold Rings, ',
             'four Calling Birds, ',
             'three French Hens, ',
             'two Turtle Doves, ',
             'and a Partridge in a Pear Tree.\n']
    on_text = 'On the {} day of Christmas my true love gave to me, '.format(days[-day_number])
    gifts_text =  ''.join(gifts[-day_number:])
    if day_number == 1:
        gifts_text = gifts_text.replace('and ', '')
    return on_text + gifts_text


def verses(start, end):
    return '\n'.join([verse(n) for n in range(start, end + 1)]) + '\n'


def sing():
    return verses(1, 12)
