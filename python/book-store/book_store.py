def take_unique(books):
    uniques = []
    remainder = []
    for book in books:
        if book in uniques:
            remainder.append(book)
        else:
            uniques.append(book)
    return uniques, remainder


def calculate_total(books):
    if not books:
        return 0
    set_prices = dict(zip(range(1, 6),
                          [8, 16*0.95, 24*0.9, 32*0.8, 40*0.75]))
    set_sizes = []
    while books:
        uniq, books = take_unique(books)
        set_sizes.append(len(uniq))
    new_price = sum([set_prices[ss] for ss in set_sizes])
    while max(set_sizes) - min(set_sizes) > 1:
        orig_price = new_price
        set_sizes.sort()
        set_sizes[0] += 1
        set_sizes[-1] -= 1
        new_price = sum([set_prices[ss] for ss in set_sizes])
        if orig_price < new_price:
            return orig_price
    return new_price
