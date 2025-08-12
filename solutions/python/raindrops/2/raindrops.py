def convert(num):
  
    final_str = ""
    if num % 3 == 0:
        final_str += "Pling"
       
    if num % 5 == 0:
        final_str += "Plang"
     
    if num % 7 == 0:
        final_str += "Plong"
     
    return final_str if final_str else str(num)
