def append(list1, list2):
    return list1 + list2


def concat(lists):
    newlist = list()
    for lis in lists:
        if len(lis) > 0:
            newlist += lis
    return newlist


def filter(function, list):
    list1 = []
    for items in list:
        if function(items):
            list1.append(items)
    return list1


def length(list):
    count = 0
    for item in list:
        count+=1
    return count


def map(function, list):
    listnew = []
    for item in list:
        listnew.append(function(item))
    return listnew


def foldl(function, list, initial):
    acc = initial
    for element in list:
        acc = function(acc,element)
    return acc


def foldr(function, list, initial):
    acc = initial
    for element in reversed(list):
        acc = function(acc,element)
    return acc


def reverse(list):
    newlist = []
    for item in range(len(list)-1,-1,-1):
        newlist.append(list[item])
    return newlist
