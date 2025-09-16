NUMBER_0_19 = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",14: "fourteen", 15: "fifteen", 16: "sixteen",17: "seventeen", 18: "eighteen", 19: "nineteen"}
UNITS = ["", "thousand", "million", "billion", "trillion"]
TENS = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
def say_under_1000(number):
    if number < 20:
        return f"{NUMBER_0_19[number]}"
    if number < 100:
        ten, unit = divmod(number, 10)
        ten_word = TENS[ten * 10]
        return ten_word if unit == 0 else f"{ten_word}-{NUMBER_0_19[unit]}"
    hundred, rem = divmod(number,100)
    if rem == 0:
        return f"{NUMBER_0_19[hundred]} hundred"
    return f"{NUMBER_0_19[hundred]} hundred {say_under_1000(rem)}"
def say(number):
    if not (0 <= number < 1_000_000_000_000):
        raise ValueError("input out of range")
    if number == 0:
        return "zero"
    chunks = []
    while number> 0:
        number,rem = divmod(number,1000)
        chunks.append(rem)
    result = []
    for i, chunk in enumerate(chunks):
        if chunk == 0:
            continue
        result.append(f"{say_under_1000(chunk)} {UNITS[i]}".strip())
    return " ".join( reversed(result))