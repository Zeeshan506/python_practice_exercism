def translate(text):
    def single(text):
        vowels = "aeiou"
        if text[0] in vowels or text.startswith("xr") or text.startswith("yt") or text.startswith("ay"):
            piglatin = text + "ay"
            return piglatin
        if not text[0] in vowels:
            index = 0            
            while index < len(text):
                ch = text[index]
                if ch == 'y' and index != 0:
                    break
                if ch in vowels:
                    break
                if ch == 'q' and index+1 < len(text) and text[index+1] == 'u':
                    index += 2
                    break
                index += 1
            text = text[index:] + text[:index] + "ay"
            return text
    
    sentence = False
    for ch in text:
        if ch == " ":
            sentence = True
    if sentence:
        return " ".join(single(word.lower()) for word in text.split())
            
    return single(text.lower())
    
       
 