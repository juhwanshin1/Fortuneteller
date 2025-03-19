import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def format_resistance(value):
    if value >= 1_000_000:
        return f"{value / 1_000_000}MΩ"
    elif value >= 1_000:
        return f"{value / 1_000}kΩ"
    return f"{value}Ω"

def resistor_value():
    color_codes = {
        "검정": 0, "갈색": 1, "빨강": 2, "주황": 3, "노랑": 4,
        "초록": 5, "파랑": 6, "보라": 7, "회색": 8, "흰색": 9
    }
    multiplier_codes = {
        "검정": 1, "갈색": 10, "빨강": 100, "주황": 1_000, "노랑": 10_000,
        "초록": 100_000, "파랑": 1_000_000, "보라": 10_000_000,
        "회색": 100_000_000, "흰색": 1_000_000_000, "금": 0.1, "은": 0.01
    }
    tolerance_codes = {
        "갈색": 1, "빨강": 2, "초록": 0.5, "파랑": 0.25,
        "보라": 0.1, "회색": 0.05, "금": 5, "은": 10
    }
    color_styles = {
        "검정": Fore.BLACK, "갈색": Fore.LIGHTBLACK_EX, "빨강": Fore.RED, "주황": Fore.LIGHTRED_EX, 
        "노랑": Fore.YELLOW, "초록": Fore.GREEN, "파랑": Fore.BLUE, "보라": Fore.MAGENTA, 
        "회색": Fore.LIGHTWHITE_EX, "흰색": Fore.WHITE, "금": Fore.LIGHTYELLOW_EX, "은": Fore.LIGHTCYAN_EX
    }
    
    print("사용 가능한 색상: ")
    for color in color_codes.keys():
        print(f"{color_styles[color]}{color}{Style.RESET_ALL}", end=" ")
    print("금 은")
    
    band_count = input("\n저항기의 색 띠 개수를 입력하세요 (4 또는 5): ")
    
    if band_count not in ["4", "5"]:
        return "잘못된 입력입니다. 4 또는 5를 입력하세요."
    
    band_count = int(band_count)
    colors = input(f"저항기의 {band_count}개 색상을 공백으로 구분하여 입력하세요: ").split()
    
    if len(colors) != band_count:
        return "입력한 색상 개수가 올바르지 않습니다."
    
    try:
        colored_input = " ".join([color_styles.get(color, "") + color + Style.RESET_ALL for color in colors])
        print(f"입력된 색상: {colored_input}")
        
        if band_count == 4:
            value = (color_codes[colors[0]] * 10 + color_codes[colors[1]]) * multiplier_codes[colors[2]]
            tolerance = tolerance_codes.get(colors[3], None)
        else:
            value = (color_codes[colors[0]] * 100 + color_codes[colors[1]] * 10 + color_codes[colors[2]]) * multiplier_codes[colors[3]]
            tolerance = tolerance_codes.get(colors[4], None)
        
        formatted_value = format_resistance(value)
        if tolerance:
            return f"저항값: {formatted_value} ±{tolerance}%"
        return f"저항값: {formatted_value}"
    except KeyError:
        return "유효하지 않은 색상이 포함되어 있습니다."
    
# 실행 예시
print(resistor_value())