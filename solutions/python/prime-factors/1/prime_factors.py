def factors(value):
    result = []
    prime = 2
    while value > 1:
        while value % prime == 0:
            result.append(prime)
            value = value // prime
        prime += 1
    return result
            
            