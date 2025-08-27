def find(search_list, value, offset = 0):
    if len(search_list) == 0:
        raise ValueError("value not in array")  
        
    center = len(search_list)//2 
    # return the center
    if  search_list[center] == value:
        return center + offset
    # if go right cal the offset, since it changes
    elif search_list[center] < value:
        return find(search_list[center+1:],value,offset+center+1)
    # if going left, indices remain the same.
    else:
        return find(search_list[:center],value,offset)
        
        
    
