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
        if operator == 'plus':
            operand += operand_2
        elif operator == 'minus':
            operand -= operand_2
        elif operator == 'multiplied by':
            operand *= operand_2
        elif operator == 'divided by':
            operand /= operand_2
        else:
            raise ValueError
        if rest == '?':
            is_continuing = False
    return operand
