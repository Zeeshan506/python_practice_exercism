def commands(binary_str):
    action_list = ["wink","double blink","close your eyes","jump"]
    result = list()
    number = int(binary_str,2)
    for index, item in enumerate(action_list):
        if number & (1 << index):
            result.append(item)
    if number & (1 << 4):
        result.reverse()
    return result  