def get_part(number, part):
    number = number % 1000000000000
    _to_slice = {'b': slice(0, 3),
                 'm': slice(3, 6),
                 't': slice(6, 9),
                 'o': slice(9, 12)}
    return int(str(number).rjust(12, '0')[_to_slice[part]])


def part_say(number, part):
    number = number % 1000
    hundreds, tens, ones = [int(d) for d in str(number).rjust(3, '0')]
    ones_map = dict(zip('123456789',
                        'one two three four five six seven eight nine'.split()))
    tens_map = dict(zip('23456789',
                        'twenty thirty forty fifty sixty seventy eighty ninety'.split()))
    teens_map = dict(zip('0123456789',
                        'ten eleven twelve thirteen fourteen fifteen sixteen seventeen '
                        'eighteen nineteen'.split()))
    part_map = {'b': ' billion ', 'm': ' million ', 't': ' thousand ', 'o': ''}
    say = ''
    if hundreds:
        say += ones_map[str(hundreds)] + ' hundred'
        if tens or ones:
            say += ' and '
    if tens == 1:
        say += teens_map[str(ones)]
    if tens > 1:
        say += tens_map[str(tens)]
        if ones:
            say += '-'
    if ones and tens != 1:
        say += ones_map[str(ones)]
    if say:
        say += part_map[part]
    return say


def say(number):
    if number > 999999999999 or number < 0:
        raise AttributeError('number must be positive and under 1 trillion')
    if number == 0:
        return 'zero'
    b, m, t, o = [part_say(get_part(int(number), prt), prt) for prt in ['b', 'm', 't', 'o']]
    if (b or m or t) and o:
        if 0 < get_part(number, 'o') < 100:
            o = 'and ' + o
    return ''.join([b, m, t, o]).strip()
