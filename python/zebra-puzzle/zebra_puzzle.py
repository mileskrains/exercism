import itertools

'''problem data setup'''

houses_pattern = [[str(n + 1)] + [None] * 5 for n in range(5)]

data = (
    'number 1 2 3 4 5',
    'color yellow blue red ivory green',
    'nationality norwegian ukranian englishman spaniard japanese',
    'drink water tea milk orange-juice coffee',
    'smoke kool chesterfield old-gold lucky-strike parliament',
    'pet fox horse snails dog zebra',
)

spec_texts = (
    'englishman red',
    'spaniard dog',
    'coffee green',
    'ukranian tea',
    'ivory, green',
    'old-gold snails',
    'kool yellow',
    'milk 3',
    'norwegian 1',
    'chesterfield, fox',
    'kool, horse',
    'lucky-strike orange-juice',
    'japanese parliament',
    'norwegian, blue',
)

invariants_texts = (
    'ivory, green',
)

incomplete_indices = (3, 5)  # we are solving for a drink and a pet
complete_indices = [i for i in range(1, 5) if i not in incomplete_indices]

data_dict = {}
for line in data:
    dat = line.split()
    data_dict[dat[0]] = dat[1:]

data_ordering = list(data_dict.keys())
val_key_dict = {}
for k, v in data_dict.items():
    for val in v:
        val_key_dict[val] = k

'''implementation functions'''


def _text_to_cond(spec_text):
    cond = [None] * 6
    vals = spec_text.split()
    for val in vals:
        key = val_key_dict[val]
        cond[data_ordering.index(key)] = val
    return cond


def text_to_cond(spec_text):
    return list(map(_text_to_cond, spec_text.split(',')))


def _compare_conds(condA, condB):
    match = False
    fill = 0
    fit = True
    for cAe, cBe in zip(condA, condB):
        if cAe and cAe == cBe:
            match = True
        if bool(cAe) != bool(cBe):  # clever XOR
            fill += 1
        if cAe and cBe and cAe != cBe:
            fit = False
    if match:
        return 'match'
    elif fill == 6:
        return 'fill'
    elif fit:
        return 'fit'
    else:
        return 'fail'


def _invariant_is_violated(cond_list):
    for inv in invariants_lists:
        match = False
        res = [_compare_conds(inv[ci], c) for ci, c in enumerate(cond_list)]
        res_w_rev = res + [_compare_conds(inv[1 - ci], c) for ci, c in enumerate(cond_list)]
        if 'match' in res_w_rev and 'fail' in res:
            return True
    return False


def _classify_cond_list_at_pos(target, cond_list, pos):
    # compound conds are left aligned
    if len(cond_list) == 2:
        if pos == 4:
            pos = 3
        if _invariant_is_violated(cond_list):
            return 'fail'
    res = [_compare_conds(target[pos + ci], c) for ci, c in enumerate(cond_list)]
    if 'fail' in res:
        return 'fail'
    if 'match' in res:
        return 'match'
    elif 'fill' in res:
        return 'fill'
    else:
        return 'fit'


def flip_cond_list_if_allowed(cond_list):
    if len(cond_list) == 1:
        return cond_list
    cl_rev = cond_list[::-1]
    if not _invariant_is_violated(cl_rev):
        return cl_rev
    return cond_list


def classify_cond_list_at_pos(target, cond_list, pos):
    if pos + len(cond_list) > len(target):
        pos -= 1
    target = target[pos:pos + len(cond_list)]
    res = _classify_cond_list_at_pos(target, cond_list, 0)
    cl_rev = flip_cond_list_if_allowed(cond_list)
    if cl_rev != cond_list:
        res_flipped = _classify_cond_list_at_pos(target, cl_rev, 0)
        if res == 'fail':
            return res_flipped
        elif res == 'fit' and res_flipped == 'fill':
            return res_flipped
        elif res == 'fill' and res_flipped == 'match':
            return res_flippped
    return res


def find_mergeable_conditions():
    # finds overlapping condition lists
    mergeable_lists = []
    for cla in all_cond_lists:
        for clb in all_cond_lists:
            if cla != clb and len(cla) < len(clb):
                for pos in (0, 1):
                    res = classify_cond_list_at_pos(clb, cla, pos)
                    if res == 'match':
                        mergeable_lists.append([clb, cla])
    return mergeable_lists


def merge_at_match(clb, cla):
    clb = clb[:]
    # a into b, if len are equal, position is 0, else must find if pos is 0 or 1
    match_pos = 0
    if len(cla) == 1 and len(clb) == 2:
        if _compare_conds(clb[1], cla[0]) == 'match':
            match_pos = 1
    for cli, cl in enumerate(cla):
        clb[match_pos + cli] = [c if c else cl[i]
                                for i, c in enumerate(clb[match_pos + cli])]
    return clb


def merge_conditions_where_possible():
    for mcs in find_mergeable_conditions():
        clb, cla = mcs
        clb_new = (merge_at_match(clb, cla))
        all_cond_lists.remove(cla)
        clb_loc = all_cond_lists.index(clb)
        all_cond_lists[clb_loc] = clb_new


def merge_to_houses(houses, cl, pos):
    houses = houses[:]
    houses[pos:pos + len(cl)] = merge_at_match(houses[pos:pos + len(cl)], cl)
    return houses


def merge_matching_conds_into_houses(houses):
    houses = houses[:]
    merge_clis = []
    for hi, _ in enumerate(houses):
        for cli, cl in enumerate(all_cond_lists):
            res = classify_cond_list_at_pos(houses, all_cond_lists[cli], hi)
            if res == 'match':
                merge_clis.append((cli, hi))
    for cli, hi in sorted(merge_clis, reverse=True):
        houses = merge_to_houses(houses, all_cond_lists[cli], hi)
        del all_cond_lists[cli]
    return houses


def merge_conditions_fitting_single_spot_into_houses(houses):
    houses = houses[:]
    merge_clis = []
    for cei in complete_indices:
        clis_with_ce = [cli
                        for cli, cl in enumerate(all_cond_lists)
                        if any([c[cei] for c in cl])]
        for hi in range(5):
            if not houses[hi][cei]:  # not already populated
                fit_res = [classify_cond_list_at_pos(houses, all_cond_lists[cli], hi)
                           for cli in clis_with_ce]
                if fit_res.count('fit') == 1:
                    fit_cli = clis_with_ce[fit_res.index('fit')]
                    merge_clis.append((fit_cli, hi))
    for cli, hi in sorted(merge_clis, reverse=True):
        houses = merge_to_houses(houses, all_cond_lists[cli], hi)
        del all_cond_lists[cli]
    return houses


def see_houses_and_all_cond_list():
    for hi, h in enumerate(houses):
        print('-' * 71, hi)
        print('|'.join([f'{ce:<12}' if ce else ' ' * 12 for ce in h]))
    print('\n\n')
    for cli, cl in enumerate(all_cond_lists):
        print('-' * 71, cli)
        for c in cl:
            print('|'.join([f'{ce:<12}' if ce else ' ' * 12 for ce in c]))


def test_trial_position(tps):
    global houses_solution
    test_houses = houses[:]
    try:
        for cli, clp in enumerate(tps):
            test_houses = merge_to_houses(test_houses, all_cond_lists[cli], clp)
        none_count = sum([h.count(None) for h in test_houses])
        if none_count == 2:
            houses_solution = test_houses
        return none_count
    except IndexError:
        pass


def solution():
    global houses_solution
    drink_index = 3
    pet_index = 5
    for house in houses_solution:
        if house[drink_index] is None:
            water_drinker = house[2].capitalize()
        if house[pet_index] is None:
            zebra_keeper = house[2].capitalize()
    return (f'It is the {water_drinker} who drinks the water.\n'
            f'The {zebra_keeper} keeps the zebra.')


'''execution'''

all_cond_lists = list(map(text_to_cond, spec_texts))
invariants_lists = list(map(text_to_cond, invariants_texts))
merge_conditions_where_possible()
houses = houses_pattern[:]
houses = merge_matching_conds_into_houses(houses)
houses = merge_conditions_fitting_single_spot_into_houses(houses)

houses_solution = []

fit_locs = [[hi for hi in range(5) if classify_cond_list_at_pos(houses, cl, hi) == 'fit']
            for cl in all_cond_lists]
trial_positions = list(itertools.product(*fit_locs))
trial_positions = [tps for tps in trial_positions
                   if set(tps) == set((0, 1, 2, 3, 4))]
for tp in trial_positions:
    if test_trial_position(tp) == 2:
        break

all_cond_lists = [flip_cond_list_if_allowed(cond_list) for cond_list in all_cond_lists]
fit_locs = [[hi for hi in range(5) if classify_cond_list_at_pos(houses, cl, hi) == 'fit']
            for cl in all_cond_lists]
trial_positions = list(itertools.product(*fit_locs))
trial_positions = [tps for tps in trial_positions
                   if set(tps) == set((0, 1, 2, 3, 4))]
for tp in trial_positions:
    if test_trial_position(tp) == 2:
        break

houses = houses_solution
# see_houses_and_all_cond_list()
solution()
