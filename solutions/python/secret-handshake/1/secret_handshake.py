def commands(binary_str):
    action_list = ["wink","double blink","close your eyes","jump","reverse"]
    number = int(binary_str)
    reverse_flag = True
    result = list()
    if number >= 10000:
        reverse_flag = False
        number -= 10000
    if number >= 1000:
        result.append(action_list[-2])
        number -= 1000
    if number >= 100:
        result.append(action_list[-3])
        number -= 100
    if number >= 10 :
        result.append(action_list[1])
        number -= 10
    if number == 1 :
        result.append(action_list[0])
    if(reverse_flag):
        result = result[::-1]
    return result
        
        
    
        
