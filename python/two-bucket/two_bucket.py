def do_op(b1, b2, op):
    c1, s1 = b1
    c2, s2 = b2
    if op == 'f':
        return (s1, s1), (c2, s2)
    elif op == 'e':
        return (c1, s1), (0, s2)
    elif op == 't':
        e2 = s2 - c2
        t = c1 if c1 <= e2 else e2
        return (c1 - t, s1), (c2 + t, s2)


def two_bucket(bucket_one_cap, bucket_two_cap, desired_liters, first):
    c1, c2 = bucket_one_cap, bucket_two_cap
    if first == 'two':
        c1, c2 = c2, c1
    b1 = 0, c1
    b2 = 0, c2
    op_ct = 0
    while not desired_liters in (b1[0], b2[0]):
        if b1[0] == 0:
            b1, b2 = do_op(b1, b2, 'f')
            op_ct += 1
        elif b2[0] == b2[1]:
            b1, b2 = do_op(b1, b2, 'e')
            op_ct += 1
        else:
            b1, b2 = do_op(b1, b2, 't')
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

