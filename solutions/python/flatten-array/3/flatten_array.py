def flatten(iterable):
    flat_list = list()
    for item in iterable:
        if isinstance(item, list):
            flat_list.extend(flatten(item)) 
        elif not item is None:
            flat_list.append(item)
    return flat_list            
