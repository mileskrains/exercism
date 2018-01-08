def find_minimum_coins(total_change, coins):
    if not total_change:
        return []
    elif total_change in coins:
        return [total_change]
    elif total_change < min(coins):
        return -1

    coins = [c for c in coins if c <= total_change]
    coins.sort()
    tries = []
    ans = -1
    len_ans = total_change // min(coins) + 1
    for coin in coins:
        tries.append([coin])

    while tries:
        change = tries.pop()
        if len(change) + 1 < len_ans:
            for coin in coins:
                if coin <= change[-1]:
                    if sum(change) + coin == total_change:
                        change.append(coin)
                        if len(change) < len_ans:
                            ans = sorted(change)
                            len_ans = len(change)
                    elif sum(change) + coin < total_change:
                        tries.append(change + [coin])
    return ans

