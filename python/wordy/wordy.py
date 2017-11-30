def split_on_digit(q):
    f = 'X'
    fa = ''
    while f.isalpha():
        fa = fa + ' ' + f
        f, q = q.split(maxsplit=1)
    return fa[3:], int(f), q

def calculate(question):
    q = question.replace('?', ' ?')
    _, operand, rest = split_on_digit(q)
    is_continuing = True
    while is_continuing:
        operator, operand_2, rest = split_on_digit(rest)
        operand = {'plus': operand + operand_2,
                   'minus': operand - operand_2,
                   'multiplied by': operand * operand_2,
                   'divided by': operand / operand_2}.get(operator, 'BAD')
        if operand == 'BAD':
            raise ValueError
        if rest == '?':
            is_continuing = False
    return operand
