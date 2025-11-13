def slices(series, length):
    # Errors
    if len(series) <= 0:
        raise ValueError("series cannot be empty")
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    # Slice The String
    results = list()
    for x in range(len(series)):
        results.append(series[x:x+length])
    filter = list()
    #Filter len:Strings == length 
    for sub in results:
        if len(sub)==length:
            filter.append(sub)
    return filter