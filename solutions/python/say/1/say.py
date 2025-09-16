NUMBER_0_19 = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",14: "fourteen", 15: "fifteen", 16: "sixteen",17: "seventeen", 18: "eighteen", 19: "nineteen"}
units = ["", "thousand", "million", "billion", "trillion"]
TENS = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
def get_tens(number):
    ten_parts = (number // 10) * 10 # return 2 for 25 and then becomes 20
    unit = number % 10
    if unit == 0:
        return TENS[ten_parts]
    return f"{TENS[ten_parts]}-{NUMBER_0_19[unit]}"
def get_hundred(number):
    hundred_part = number // 100
    remaining = number % 100
    if remaining == 0:
        return f"{NUMBER_0_19[hundred_part]} hundred"
    else:
        # Use get_tens if remaining >= 20 else direct lookup
        if remaining < 20:
            return f"{NUMBER_0_19[hundred_part]} hundred {NUMBER_0_19[remaining]}"
        else:
            return f"{NUMBER_0_19[hundred_part]} hundred {get_tens(remaining)}"
def chunker(number):
    num_str = str(number)
    # pad with leading zeros to make length multiple of 3
    padded = num_str.zfill(((len(num_str)+2)//3)*3)
    chunks = [int(padded[i:i+3]) for i in range(0, len(padded), 3)]
    return chunks
def say_help(number):
    if number < 20:
        return NUMBER_0_19[number]
    elif number < 100:
        return get_tens(number)
    elif number <= 999:
        return get_hundred(number)
def say(number):
    if number < 0 or number >= 1_000_000_000_000:
        raise ValueError("input out of range")
    if number == 0:
        return NUMBER_0_19[number]
    chunks = chunker(number)
    num_chunks = len(chunks)
    words = []
    for i, chunk in enumerate(chunks):
        if chunk == 0:
            continue  # skip zeros
        chunk_words = say_help(chunk)
        unit = units[num_chunks - i - 1]  # right-to-left mapping
        if unit:
            words.append(f"{chunk_words} {unit}")
        else:
            words.append(f"{chunk_words}")
    return " ".join(words)