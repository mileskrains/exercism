def transform(legacy_data):
    data = {}
    for k, v in legacy_data.items():
        for c in v:
            data[c.lower()] = k
    return data
