def do_op(b1, b2, op):
    c1, s1 = b1
    c2, s2 = b2
    if op == 'fill':
        return (s1, s1), (c2, s2)
    elif op == 'empty':
        return (c1, s1), (0, s2)
    elif op == 'transfer':
        e2 = s2 - c2
        t = c1 if c1 <= e2 else e2
        return (c1 - t, s1), (c2 + t, s2)


def two_bucket(bucket_one_cap, bucket_two_cap, desired_liters, first):
    b1 = 0, bucket_one_cap
    b2 = 0, bucket_two_cap
    if first == 'two':
        b1, b2 = b2, b1
    op_ct = 0
    while not desired_liters in (b1[0], b2[0]):
        if b1[0] == 0:
            b1, b2 = do_op(b1, b2, 'fill')
        elif b2[0] == b2[1]:
            b1, b2 = do_op(b1, b2, 'empty')
        else:
            b1, b2 = do_op(b1, b2, 'transfer')
        op_ct += 1
    if first == 'two':
        b1, b2 = b2, b1
    if b1[0] == desired_liters:
        dl_bucket = 'one'
        rem = b2[0]
    else:
        dl_bucket = 'two'
        rem = b1[0]
    return op_ct, dl_bucket, rem

