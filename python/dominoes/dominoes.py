def chain(dominoes):
    if dominoes == []:
        return []
    chain, remainder = dominoes[:1], dominoes[1:]
    tries = [(chain, remainder)]
    while tries:
        chain, remainder = tries.pop()
        if remainder == [] and chain[0][0] == chain[-1][1]:
            return chain
        match_val = chain[-1][1]
        links = [dom for dom in remainder if match_val in dom]
        if links:
            for link in links:
                new_remainder = remainder.copy()
                new_remainder.remove(link)
                if link[1] == match_val:
                    link = tuple(reversed(link))
                tries.append((chain + [link], new_remainder))