def flatten(iterable, flattened=None):
    if flattened == None:
        flattened = []
    for it in iterable:
        if type(it) in (list, set, tuple):
            flatten(it, flattened)
        else:
            flattened.append(it)
    return [el for el in flattened if el is not None]
