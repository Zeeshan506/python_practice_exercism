def find_anagrams(word, candidates):
    sorted_word = "".join(sorted(word.lower()))
    result = []
    for candidate in candidates:
        if candidate.lower() == word.lower():
            continue
        words_sorted = "".join(sorted(candidate.lower()))
        if words_sorted == sorted_word:
            print(candidate)
            result.append(candidate)
    return result
            