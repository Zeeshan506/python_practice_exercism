def convert(num):
    flag = False
    final_str = ""
    if num % 3 == 0:
        final_str += "Pling"
        flag = True
    if num % 5 == 0:
        final_str += "Plang"
        flag = True
    if num % 7 == 0:
        final_str += "Plong"
        flag = True

    if flag:
        return final_str
    return str(num)
