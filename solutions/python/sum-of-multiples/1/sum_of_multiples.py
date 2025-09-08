def get_multiple_set(limit,multiple):
    if multiple == 0:
        return set()
    multi_set = set()
    for index in range(1 ,limit):
        if index % multiple == 0:
            multi_set.add(index)  
    return multi_set
    
def sum_of_multiples(limit, multiples):
    sum_res = 0
    new_set = set()
    for multiple in multiples:
        ret_res = get_multiple_set(limit,multiple)
        new_set.update(ret_res)
    sum_res += sum(new_set)   
    return sum_res
