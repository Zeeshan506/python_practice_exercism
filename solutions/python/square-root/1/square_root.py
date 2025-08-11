def square_root(number):
    if number <= 0:
        raise ValueError ("Only Positive numbers are accepted")
    if number == 1:
        return 1
    for index in range(number):
        if index * index == number:
            return index
    return None