def square_of_sum(number):
    sum = 0
    for index in range(1,number+1):
        sum += index
    return sum ** 2


def sum_of_squares(number):
    sum = 0
    for index in range(1,number+1):
        sum += (index ** 2)
    return sum
    


def difference_of_squares(number):
    sum_of = sum_of_squares(number)
    square_of = square_of_sum(number)
    return square_of - sum_of
