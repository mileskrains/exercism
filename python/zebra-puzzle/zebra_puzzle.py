data_sets = (
    'yellow blue red ivory green',
    'norwegian ukranian englishman spaniard japanese',
    'water tea milk orange-juice coffee',
    'kool chesterfield old-gold lucky-strike parliament',
    'fox horse snails dog zebra',
)

data_specs = (
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

data_specs_inv = (
    'ivory, green',
)


def find_available_values(item):
    for ds in data_sets:
        if item in ds:
            used = [known[d] for d in ds]
            unused = [n for n in range(1, 6) if n not in used]
            break
    for ds in data_specs_inv:
        if item in ds:
            a, b = ds.split(', ')
            ka, kb = known[a], known[b]
            if item == a and kb:
                if kb - 1 in unused:
                    return [kb - 1]
                else:
                    return []
            if item == b and ka:
                if ka + 1 in unused:
                    return [ka + 1]
                else:
                    return []
    for ds in data_specs:
        if item in ds:
            if ',' in ds:
                a, b = ds.split(', ')
                if a == item:
                    a, b = b, a
                aval = known[a]
                if aval:
                    return [v for v in [aval-1, aval+1] if v in unused]
            else:
                a, b = ds.split()
                if a == item:
                    a, b = b, a
                aval = known[a]
                if aval:
                    return [aval]
    return unused


def process_specs():
    for sp in data_specs:
        clauses = sp.split(', ')
        if len(clauses) == 2:
            a, b = clauses
            if known[a]:
                a, b = b, a
            if not known[a]:
                a_poss = find_available_values(a)
                if len(a_poss) == 1:
                    known[a] = a_poss[0]
        else:
            for cl in clauses:
                eqs = cl.split()
                if len(eqs) == 2:
                    a, b = eqs
                    if b.isdigit():
                        known[a] = int(b)
                    elif known[a]:
                        known[b] == known[a]
                    elif known[b]:
                        knowns[a] == known[b]


def item_nationality(item):
    item_house = known[item]
    return [nat for nat in data_sets[1] if known[nat] == item_house][0]


def solution():
    return (f"It is the {item_nationality('water').capitalize()} who drinks the water.\n"
            f"The {item_nationality('zebra').capitalize()} keeps the zebra.")


data_sets = [ds.split() for ds in data_sets]
known = dict()
for ds in data_sets:
    for item in ds:
        known[item] = 0
for _ in range(5):
    process_specs()
unknown = [k for k, v in known.items() if not v]
known_orig = known.copy()

try_item = unknown.pop(0)
try_val_lists = [[(try_item, av)] for av in find_available_values(try_item)]
found = False
while not found and try_val_lists:
    known = known_orig.copy()
    tvl = try_val_lists.pop(0)
    for item, try_val in tvl:
        known[item] = try_val
    unknown = [k for k, v in known.items() if not v]
    try_item = unknown.pop(0)
    for av in find_available_values(try_item):
        if unknown == []:
            found = True
        try_val_lists.append(tvl + [(try_item, av)])

known = known_orig.copy()
tvl = try_val_lists.pop()
for item, try_val in tvl:
    known[item] = try_val

print(solution())