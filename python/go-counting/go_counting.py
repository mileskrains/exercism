from collections import defaultdict

BLACK = 'B'
WHITE = 'W'
NONE = ''


class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.board = board
        self.board_dict = defaultdict(str)
        for rn, row in enumerate(board.split('\n')):
            for cn, cv in enumerate(row):
                self.board_dict[cn, rn] = cv

    def territoryFor(self, coord):
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            coord ((int,int)): Coordinate on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        c, r = coord
        if not self.board_dict[c, r] == ' ':
            return '', set()
        cr_offsets = ((-1, 0), (0, 1), (1, 0), (0, -1))
        unvisited = [coord]
        visited = []
        territory = set()
        bordering = set()
        while unvisited:
            c, r = unvisited.pop()
            visited.append((c, r))
            territory.add((c, r))
            for co, ro in cr_offsets:
                nc, nr = c + co, r + ro
                if (nc, nr) in visited:
                    continue
                nv = self.board_dict[nc, nr]
                if nv == ' ':
                    unvisited.append((nc, nr))
                elif nv in ('W', 'B'):
                    bordering.add(nv)
                    visited.append((nc, nr))
        stone = bordering.pop() if len(bordering) == 1 else ''
        return stone, territory

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        territories = {'': set(), 'W': set(), 'B': set()}
        checked = []
        for (c, r), v in list(self.board_dict.items()):
            if v == ' ' and (c, r) not in checked:
                stone, territory = self.territoryFor((c, r))
                territories[stone].update(territory)
                checked.extend(list(territory))
        return dict(territories)

