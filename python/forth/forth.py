class StackUnderflowError(Exception):
    pass


def stack_pop(stack):
    try:
        r = stack.pop()
    except:
        raise StackUnderflowError('op needs more args')
    else:
        return r, stack


def do_op(op, stack):
    op = op.upper()
    x, stack = stack_pop(stack)
    if op not in ('DUP', 'DROP'):
        y, stack = stack_pop(stack)
    if op == 'DUP':
        stack.append(x)
        stack.append(x)
    elif op == 'DROP':
        pass
    elif op == 'SWAP':
        stack.append(x)
        stack.append(y)
    elif op == 'OVER':
        stack.append(y)
        stack.append(x)
        stack.append(y)
    elif op == '+':
        stack.append(y + x)
    elif op == '-':
        stack.append(y - x)
    elif op == '*':
        stack.append(y * x)
    elif op == '/':
        stack.append(y // x)
    return stack


def add_definition(def_string, def_dict):
    _, name, *sub, _ = def_string.split()
    if name.isdigit():
        raise ValueError('cannot redefine numbers')
    def_dict[name.upper()] = [validate(el, def_dict) for el in sub]
    return def_dict


def validate(el, def_dict):
    ops = 'DUP DROP SWAP OVER + - * /'
    if (el.isdigit() or
            el.upper() in ops or
            el.upper() in def_dict):
        return el
    else:
        raise ValueError('unknown word')


def parse(line, def_dict):
    els = [validate(el, def_dict) for el in line.split()]
    seq = []
    for el in els:
        if el.upper() in def_dict:
            seq.extend(def_dict[el.upper()])
        else:
            seq.append(el)
    return seq


def evaluate(input_data):
    stack = []
    def_dict = {}
    for line in input_data:
        if line and line[0] == ':':
            def_dict = add_definition(line, def_dict)
            line_seq = []
        else:
            line_seq = parse(line, def_dict)
        for el in line_seq:
            if el.isdigit():
                stack.append(int(el))
            else:
                stack = do_op(el, stack)
    return stack