SUBLIST = "sub"
SUPERLIST = "sup"
EQUAL = "equ" 
UNEQUAL = "une"
def is_sublist(big,small):
    if len(small) == 0:
        return True
    return any(big[index: index + len(small)] == small
                for index in range(len(big) - len(small) + 1))
def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if len(list_one) > len(list_two):
        if is_sublist(list_one,list_two):
            return SUPERLIST
        return UNEQUAL
    if len(list_one) < len(list_two):
        if is_sublist(list_two,list_one):
            return SUBLIST
        return UNEQUAL
    return UNEQUAL