from string import ascii_uppercase

def make_diamond(letter):
    letters = ascii_uppercase[:ascii_uppercase.index(letter)+1]
    size = 2*len(letters)-1
    blank = [list(' ' * size) for _ in range(size)]
    for ci, ch in enumerate(letters):
        for ri in (ci, size-1-ci):
            row = blank[ri]
            row[len(letters)-1-ci] = ch
            row[-len(letters)+ci] = ch
    return '\n'.join(list(map(lambda r: ''.join(r), blank))) + '\n'

