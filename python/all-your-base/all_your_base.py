def rebase(from_base, digits, to_base):
    if min(from_base, to_base) < 2:
        raise ValueError('bases must be > 1')
    if not digits or max(digits)==0:
        return []
    dec = 0
    for di, d in enumerate(reversed(digits)):
        if d >= from_base or d < 0:
            raise ValueError('digits must be non-negative and less than base')
        dec += from_base**di * d
    pwr = 0
    while to_base**pwr < dec:
        pwr += 1
    if pwr > 0:
        pwr -= 1
    to_base_digits = []
    while pwr >= 0:
        place_val = to_base**pwr
        pwr -= 1
        rem = dec % place_val
        to_base_digits.append((dec-rem)//place_val)
        dec = rem
    return to_base_digits
