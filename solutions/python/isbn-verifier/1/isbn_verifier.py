def is_valid(isbn):
    isbn = isbn.replace("-","")
    if len(isbn) != 10:
        return False
    if not isbn[:-1].isdigit():
        return False
    if isbn[-1].isalpha():
        if not isbn[-1] == "X":
            return False
            
    isbn_list = [int(char) for char in isbn[:-1]]
    isbn_list.append(10 if isbn[-1] == "X" else int(isbn[-1]))
    total = sum( num * (10 - idx) for idx,num in enumerate(isbn_list))
    return total % 11 == 0
