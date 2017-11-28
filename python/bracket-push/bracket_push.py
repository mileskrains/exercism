def check_brackets(input_string):
    br_opening = '{[('
    br_closing = '}])'
    br_closes = dict(zip(br_closing, br_opening))
    br_stack = []
    for ch in input_string:
        if ch in br_opening:
            br_stack.append(ch)
        if ch in br_closing:
            if br_stack and br_closes[ch] == br_stack[-1]:
                br_stack.pop()
            else:
                return False
    return br_stack == []
