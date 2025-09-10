def remove_alpha(input_string):
    new_string = ""
    checker = "[]{}()"
    
    for char in input_string:
        if char in checker:
            new_string += char
    return new_string
def is_paired(input_string):
    new_string = remove_alpha(input_string)
    stack = []
    bracket_map = {
        ")":"(",
        "}":"{",
        "]":"[",
    } 
    for char in new_string:
        if char in bracket_map.values():
            stack.append(char)
        elif len(stack) == 0 or stack[-1] != bracket_map[char]:
            return False
        else:
            stack.pop()
    return len(stack) == 0 