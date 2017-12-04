class Condition():
    def __init__(self, number=None, color=None, nationality=None,
                 pet=None, beverage=None, cigarette=None):
        self.number = number
        self.color = color
        self.nationality = nationality
        self.pet = pet
        self.beverage = beverage
        self.cigarette = cigarette

    def __repr__(self):
        repr = 'COND:: '
        repr += ''.join([f'{k}: {v}, ' if v else ''
                         for k, v in self.__dict__.items()])
        return repr.strip(', ')

    def has_match(self, other):
        selfspec = [v for k, v in self.__dict__.items() if v]
        otherspec = [v for k, v in other.__dict__.items() if v]
        return bool(set(selfspec).intersection(set(otherspec)))

    def is_subset(self, other):
        selfspec = [v for k, v in self.__dict__.items() if v]
        otherspec = [v for k, v in other.__dict__.items() if v]
        return set(selfspec).issubset(set(otherspec))

    def can_combine(self, other):
        ds = self.__dict__
        do = other.__dict__
        for k, v in ds.items():
            if v:
                if do[k] and do[k] != v:
                    return False
        return True

    def combine(self, other):
        ds = self.__dict__
        do = other.__dict__
        combo = {**ds, **{k: v for k, v in do.items() if v}}
        return Condition(**combo)


# 1. are five houses
houses = [Condition(number=n + 1) for n in range(5)]

# 2. englishman lives in red house
c2 = [Condition(nationality='englishman', color='red')]

# 3. spaniard owns dog
c3 = [Condition(nationality='spaniard', pet='dog')]

# 4. coffee is drunk in the green house
c4 = [Condition(beverage='coffee', color='green')]

# 5. the ukranian drinks tea
c5 = [Condition(nationality='ukranian', beverage='tea')]

# 6. green house just right of ivory
c6 = [Condition(color='ivory'),
      Condition(color='green')]

# 7. old gold smoker keeps snails
c7 = [Condition(cigarette='old gold', pet='snails')]

# 8. kools are smoked in the yellow house
c8 = [Condition(cigarette='kools', color='yellow')]

# 9. Milk is drunk in the middle house.
c9 = [Condition(beverage='milk', number=3)]

# 10. The Norwegian lives in the first house.
c10 = [Condition(nationality='norwegian', number=1)]

# 11. The man who smokes Chesterfields lives in the house next to the man with the fox.
c11 = [Condition(cigarette='chesters'),
       Condition(pet='fox')]

# 12. Kools are smoked in the house next to the house where the horse is kept.
c12 = [Condition(cigarette='kools'),
       Condition(pet='horse')]

# 13. The Lucky Strike smoker drinks orange juice.
c13 = [Condition(cigarette='luckys', beverage='oj')]

# 14. The Japanese smokes Parliaments.
c14 = [Condition(nationality='japanese', cigarette='parliament')]

# 15. The Norwegian lives next to the blue house.
c15 = [Condition(nationality='norwegian'),
       Condition(color='blue')]

condition_lists = [c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15]
cl_is_reversible = [c11, c12, c15]


def cl_combine_if_common(cl_mrg, cl_targ):
    alignments = range(len(cl_targ) - len(cl_mrg) + 1)
    for a in alignments:
        matches = False
        combines = True

        for p, c in enumerate(cl_mrg):
            if cl_targ[a + p].has_match(c):
                matches = True
            if not cl_targ[a + p].can_combine(c):
                combines = False

        if matches and combines:
            for p, c in enumerate(cl_mrg):
                cl_targ[a + p] = cl_targ[a + p].combine(c)
            return True
    return False


def cl_combine_if_fits_one_spot(cl_mrg, cl_targ):
    alignments = range(len(cl_targ) - len(cl_mrg) + 1)
    combines_list = []
    for a in alignments:
        combines = True
        for p, c in enumerate(cl_mrg):
            if not cl_targ[a + p].can_combine(c):
                combines = False
        combines_list.append(combines)
        if combines:
            a_comb = a
        if cl_mrg in cl_is_reversible:
            combines = True
            for p, c in enumerate(list(reversed(cl_mrg))):
                if not cl_targ[a + p].can_combine(c):
                    combines = False
            combines_list.append(combines)
        if combines:
            a_comb = a

    if sum(combines_list) == 1:
        for p, c in enumerate(cl_mrg):
            cl_targ[a_comb + p] = cl_targ[a_comb + p].combine(c)


def cl_in_cl(cl_mrg, cl_targ):
    alignments = range(len(cl_targ) - len(cl_mrg) + 1)
    for a in alignments:
        is_subset = True

        for p, c in enumerate(cl_mrg):
            if not c.is_subset(cl_targ[a + p]):
                is_subset = False
        if is_subset:
            return True
    return False


def view_condition_list(condlist):
    for c in condlist:
        print([f'{v:<10}' if v else ' ' * 10 for k, v in c.__dict__.items()])


# see progress / status
view_condition_list(houses)
print()
for cl in condition_lists:
    view_condition_list(cl)
    print()

# do come merging ...
for _ in range(100):
    combined = []
    for cl in condition_lists:
        for ocl in condition_lists:
            if cl != ocl and len(cl) <= len(ocl):
                if cl_combine_if_common(cl, ocl):
                    combined.append(cl)

    condition_lists = [cl for cl in condition_lists if not cl in combined]

    for cl in condition_lists:
        cl_combine_if_fits_one_spot(cl, houses)

condition_lists = [cl for cl in condition_lists if not cl_in_cl(cl, houses)]

# see progress / status
print('\n\n\n')
view_condition_list(houses)
print()
for cl in condition_lists:
    view_condition_list(cl)
    print()
