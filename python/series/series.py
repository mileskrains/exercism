def slices(series, length):
    if length < 1 or length > len(series):
        raise ValueError('length value not workable')
    subseries = (series[i:i+length] for i in range(len(series)-length+1))
    return[[int(c) for c in sub] for sub in subseries]
