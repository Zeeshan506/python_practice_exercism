def label(colors):
    if len(colors) > 3:
        colors = colors[:3]
    def add_metric(number: int) -> str:
        if number >= 1_000_000_000:
            return f"{number // 1_000_000_000} giga"
        elif number >= 1_000_000:
            return f"{number // 1_000_000} mega"
        elif number >= 1_000:
            return f"{number // 1_000} kilo"
        else:
            return str(number) + " "
    color_map = {        
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }    
    value = int(str(color_map[colors[0]]) + str(color_map[colors[1]]))
    value *= 10 ** color_map[colors[2]]
     
    return add_metric(value) + "ohms"
        
