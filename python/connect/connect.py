from collections import defaultdict


class ConnectGame:
    def __init__(self, board):
        self.board = board
        self.board_dict = defaultdict(str)
        for rn, row in enumerate(board.split('\n')):
            for cn, cv in enumerate(row.split()):
                self.board_dict[rn, cn] = cv
        self.mri, self.mci = max(self.board_dict.keys())

    def get_winner(self):
        if self.mri == 0 and self.mci == 0:
            return self.board_dict[0, 0]

        def check():
            nonlocal winner
            vis = []
            while unvis and winner == '':
                r, c = unvis.pop()
                vis.append((r, c))
                for ro, co in move_rc_offsets:
                    tr, tc = r + ro, c + co
                    if self.board_dict[tr, tc] == win_char:
                        if (tr, tc) not in vis:
                            unvis.append((tr, tc))
                        if (tr, tc)[win_index] == win_val:
                            winner = win_char
                            break

        move_rc_offsets = ((-1, 0), (-1, 1), (0, 1), (1, 0), (1, -1), (0, -1))
        winner = ''
        win_char, win_index, win_val = 'O', 0, self.mri
        unvis = [(0, sc) for sc in range(self.mci + 1)
                 if self.board_dict[0, sc] == win_char]
        check()

        win_char, win_index, win_val = 'X', 1, self.mci
        unvis = [(sr, 0) for sr in range(self.mri + 1)
                 if self.board_dict[sr, 0] == win_char]
        check()

        return winner

