def append(xs, ys):
    total_len = length(xs) + length(ys)
    output = [None] * total_len
    for xi, x in enumerate(xs):
        output[xi] = x
    for yi, y in enumerate(ys):
        output[len(xs) + yi] = y
    return output


def concat(lists):
    output = []
    for list in lists:
        output = append(output, list)
    return output


def filter_clone(function, xs):
    output = []
    for x in xs:
        if function(x):
            output = append(output, [x])
    return output


def length(xs):
    item_ct = 0
    for item in xs:
        item_ct += 1
    return item_ct


def map_clone(function, xs):
    return [function(x) for x in xs]


def foldl(function, xs, acc):
    if xs:
        arg_zero = xs[0]
        for x in xs[1:]:
            arg_zero = function(arg_zero, x)
        return function(arg_zero, acc)
    else:
        return function(1, acc)


def foldr(function, xs, acc):
    if xs:
        arg_zero = function(xs[-1], acc)
        for x in reverse(xs[:-1]):
            arg_zero = function(x, arg_zero)
        return arg_zero
    else:
        return function(acc, 1)


def reverse(xs):
    rev = xs[:]
    for xi, x in enumerate(xs):
        rev[-xi-1] = x
    return rev
