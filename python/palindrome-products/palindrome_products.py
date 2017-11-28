def largest_palindrome(max_factor, min_factor=1):
    lpp = 0
    for x in range(min_factor, max_factor+1):
        for y in range(x, max_factor+1):
            prod = x * y
            if str(prod) == str(prod)[::-1]:
                if prod > lpp:
                    lpp = prod
                    lpp_factors = {x, y}
    return lpp, lpp_factors


def smallest_palindrome(max_factor, min_factor=1):
    spp = max_factor**2+1
    for x in range(min_factor, max_factor+1):
        for y in range(x, max_factor+1):
            prod = x * y
            if str(prod) == str(prod)[::-1]:
                if prod < spp:
                    spp = prod
                    spp_factors = {x, y}
    return spp, spp_factors
