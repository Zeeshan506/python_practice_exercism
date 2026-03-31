def is_isogram(string):
    occured = {}
    for ch in string.lower():
        if not ch.isalpha():
            continue
        if ch in occured:
            return False
        occured[ch] = 1
    return True
