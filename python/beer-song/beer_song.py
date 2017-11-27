def _bottles_text(number):
    num = str(number) if number > 0 else 'no more'
    return f'{num} bottle{"" if number==1 else "s"} of beer on the wall'


def verse(number):
    bt = _bottles_text(number)
    line_one = f'{bt.capitalize()}, {bt[:-12]}.\n'
    line_two = (f'Take {"it" if number==1 else "one"} down and pass it'
                f' around, {_bottles_text(number-1)}.\n')
    if number == 0:
        line_two = f'Go to the store and buy some more, {_bottles_text(99)}.\n'
    return line_one + line_two


def song(number1, number2=0):
    verses = ''
    for vn in range(number1, number2-1, -1):
        verses += verse(vn)+'\n'
    return verses
