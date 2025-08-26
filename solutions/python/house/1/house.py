PARTS = [
    "the house that Jack built.",
    "the malt that lay in ",
    "the rat that ate ",
    "the cat that killed ",
    "the dog that worried ",
    "the cow with the crumpled horn that tossed ",
    "the maiden all forlorn that milked ",
    "the man all tattered and torn that kissed ",
    "the priest all shaven and shorn that married ",
    "the rooster that crowed in the morn that woke ",
    "the farmer sowing his corn that kept ",
    "the horse and the hound and the horn that belonged to "
]

def build(n):
    if n == 1:
        return PARTS[0]
    return PARTS[n-1] + build(n-1)
    
def recite_one(index):
    return "This is " + build(index)

def recite(start_verse, end_verse):
    result = []
    for index in range(start_verse,end_verse+1):
        result.append(recite_one(index))
    return result
    
        
        
                
    