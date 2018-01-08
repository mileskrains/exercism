def find_minimum_coins(total_change, coins):
    if not total_change:
        return []
    elif total_change in coins:
        return [total_change]
    elif total_change < min(coins):
        return -1

    coins.sort()
    tries = []
    for coin in coins:
        tries.append([coin])
    ans = -1
    len_ans = total_change // min(coins) + 1

    while tries:
        change = tries.pop()
        if len(change) + 1 < len_ans:
            for coin in coins:
                if coin <= change[-1]:
                    if sum(change) + coin < total_change:
                        tries.append(change + [coin])
                    elif sum(change) + coin == total_change:
                        change.append(coin)
                        if len(change) < len_ans:
                            ans = sorted(change)
                            len_ans = len(change)
    return ans
