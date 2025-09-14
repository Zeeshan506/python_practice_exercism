PROTIEN_MAP= {"AUG": "Methionine","UUU": "Phenylalanine","UUC":"Phenylalanine","UUA": "Leucine","UUG": "Leucine","UCU": "Serine","UCC": "Serine","UCA": "Serine","UCG": "Serine","UAU": "Tyrosine","UAC": "Tyrosine","UGU": "Cysteine","UGC": "Cysteine","UGG": "Tryptophan","UAA": "STOP","UAG": "STOP","UGA": "STOP"}
def break_strand(strand):
    return [strand[i:i+3] for i in range(0, len(strand), 3)]
def proteins(strand):
    result = []
    broken = break_strand(strand)
    for item in broken:
        if item in PROTIEN_MAP.keys():
            if PROTIEN_MAP[item] == "STOP":
                break
            result.append(PROTIEN_MAP[item])
    return result