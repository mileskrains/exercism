from collections import defaultdict


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({}:{})'.format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not (self == other)


class WordSearch(object):
    def __init__(self, puzzle):
        self.puz_dict = defaultdict(str)
        for ln, line in enumerate(puzzle.split('\n')):
            for cn, ch in enumerate(line):
                self.puz_dict[ln, cn] = ch
        self.search_locs = list(self.puz_dict)

    def search(self, word):
        dir_offsets = ((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1))
        match = False
        for ln, cn in self.search_locs:
            if self.puz_dict[ln, cn] == word[0]:
                ws = Point(cn, ln)
                for do in dir_offsets:
                    line_offset, col_offset = do
                    match = True
                    for wchar_num, wchar in enumerate(word):
                        check_line = ln + wchar_num * line_offset
                        check_col = cn + wchar_num * col_offset
                        if self.puz_dict[check_line, check_col] != wchar:
                            match = False
                    if match:
                        wf = Point(check_col, check_line)
                        break
            if match:
                break
        return (ws, wf) if match else None
