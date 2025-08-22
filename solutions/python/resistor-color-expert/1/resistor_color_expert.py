def resistor_label(colors):
    def add_metric_whole(number: int) -> str:
        """Used for 4-band: always integer only."""
        if number >= 1_000_000_000:
            return f"{number // 1_000_000_000} gigaohms"
        elif number >= 1_000_000:
            return f"{number // 1_000_000} megaohms"
        elif number >= 1_000:
            return f"{number // 1_000} kiloohms"
        else:
            return f"{number} ohms"

    def add_metric_precise(number: int) -> str:
        """Used for 5-band: allow decimals, but trim trailing 0."""
        if number >= 1_000_000_000:
            val, unit = number / 1_000_000_000, "gigaohms"
        elif number >= 1_000_000:
            val, unit = number / 1_000_000, "megaohms"
        elif number >= 1_000:
            val, unit = number / 1_000, "kiloohms"
        else:
            return f"{number} ohms"
            
        if abs(val - round(val)) < 1e-9:
            return f"{int(round(val))} {unit}"
        else:
            return f"{val:.2f}".rstrip("0").rstrip(".") + " " + unit
    
    color_map = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
    tolerance = {
        "grey":"0.05%",
        "violet":"0.1%",
        "blue":"0.25%",
        "green":"0.5%",
        "brown":"1%",
        "red":"2%",
        "gold":"5%",
        "silver":"10%",
    }

    match len(colors):
        case 1:
            return f"{color_map.index(colors[0])} ohms"
        
        case 2:
            return f"{color_map.index(colors[0])}{color_map.index(colors[1])} ohms"
        
        case 3:
            value = int(str(color_map.index(colors[0])) + str(color_map.index(colors[1])))
            value *= 10 ** color_map.index(colors[2])
            return add_metric_whole(value)
        
        case 4:
            value = int(str(color_map.index(colors[0])) + str(color_map.index(colors[1])))
            value *= 10 ** color_map.index(colors[2])
            return add_metric_precise(value) + " ±" + tolerance[colors[3]]
        
        case 5:
            value = int(str(color_map.index(colors[0])) +
                        str(color_map.index(colors[1])) +
                        str(color_map.index(colors[2])))
            value *= 10 ** color_map.index(colors[3])
            return add_metric_precise(value) + " ±" + tolerance[colors[4]]
