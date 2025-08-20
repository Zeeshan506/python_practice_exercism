def to_rna(dna_strand):
    d_to_r_map = {
        "A":"U",
        "C":"G",
        "G":"C",
        "T":"A",
    }
    return "".join(d_to_r_map[char] for char in dna_strand)
        
