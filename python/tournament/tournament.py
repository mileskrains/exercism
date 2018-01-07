from collections import defaultdict


def tally(tournament_results):
    results = 'Team'.ljust(31, ' ') + '| MP |  W |  D |  L |  P\n'
    if not tournament_results:
        return results.strip()
    tally_dict = defaultdict(lambda : defaultdict(int))
    contests = tournament_results.split('\n')
    for contest in contests:
        p1, p2, res = contest.split(';')
        tally_dict[p1]['MP'] += 1
        tally_dict[p2]['MP'] += 1
        if res == 'loss':
            p1, p2 = p2, p1
            res = 'win'
        if res == 'win':
            tally_dict[p1]['W'] += 1
            tally_dict[p1]['P'] += 3
            tally_dict[p2]['L'] += 1
        elif res == 'draw':
            tally_dict[p1]['D'] += 1
            tally_dict[p1]['P'] += 1
            tally_dict[p2]['D'] += 1
            tally_dict[p2]['P'] += 1
    table = []
    for k, v in tally_dict.items():
        table.append([k] + [v[vk] for vk in 'MP W D L P'.split()])
    table.sort(key=lambda t: (-t[1], -t[2], -t[3], -t[4], -t[5], t[0]))
    for t, mp, w, d, l, p in table:
        results += ' |  '.join([str(val)
                                for val in (t.ljust(30, ' '), mp, w, d, l, p)]) + '\n'
    return results.strip()

