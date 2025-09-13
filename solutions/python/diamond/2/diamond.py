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
def create_string(limit,index):
        spaces = limit - index
        if index == 65:
            new_string = add_first(index,spaces)
            return new_string
        new_string = add_rest(index,spaces)
        return new_string    
def rows(letter):
    limit = ord(letter)
    result = []
    for index in range(65, limit+1):
        result.append(create_string(limit,index))
    for index in range(limit-1, 64, -1):
        result.append(create_string(limit,index))
    return result