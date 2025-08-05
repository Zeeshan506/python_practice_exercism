def is_armstrong_number(number): 
    final = number
    digit = []
    while number > 0:
        dig = number % 10
        digit.append(dig)
        number =int (number/10)
    sum = 0
    digit = digit[::-1]
    for _,value in enumerate(digit):
        sum += value ** len(digit)  
    if sum == final:
        return True
    return False
        
        
