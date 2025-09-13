def add_first(index,spaces):
    new_string = ""
    new_string = add_outer_spaces(new_string,spaces)
    new_string+= chr(index)
    new_string = add_outer_spaces(new_string,spaces)
    return new_string

def add_rest(index,spaces):
    new_string = ""
    new_string = add_outer_spaces(new_string,spaces)
    new_string += chr(index)
    new_string += (" " * (2 * (index-65) - 1))
    new_string += chr(index)
    new_string = add_outer_spaces(new_string,spaces)
    return new_string

def add_outer_spaces(string,spaces):
    return string + (" " * spaces)
    
def rows(letter):
    limit = ord(letter)
    result = []
    for index in range(65, limit+1):
        new_string = ""
        spaces = limit - index
        if index == 65:
            new_string = add_first(index,spaces)
            result.append(new_string)
            continue             
        new_string = add_rest(index,spaces)
        result.append(new_string)
    for index in range(limit-1, 64, -1):
        new_string= ""
        spaces = limit - index
        if index == 65:
            new_string = add_first(index,spaces)
            result.append(new_string)
            continue
        new_string = add_rest(index,spaces)
        result.append(new_string)

        
    print(result)
    return result
        
                


