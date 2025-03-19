import random
import datetime
from termcolor import colored  # termcolor를 임포트

def get_daily_fortune(initials):
    # 오늘 날짜를 가져옵니다
    today = datetime.date.today()

    # 날짜를 문자열로 변환 (예: 2025-03-19)
    today_str = today.isoformat()

    # 운세 리스트 (긍정적, 부정적 메시지를 혼합)
    fortunes = [
        "오늘은 새로운 시작을 위한 좋은 날입니다. 기회를 놓치지 마세요.",
        "잠시 쉬어가는 것도 좋습니다. 과로하지 않도록 주의하세요.",
        "오늘은 친구와의 만남이 좋은 결과를 가져올 것입니다.",
        "예상치 못한 기쁜 소식이 들려올 수 있습니다.",
        "오늘은 인내심을 가지고 상황을 지켜보는 것이 중요합니다.",
        "새로운 도전을 시도해도 좋습니다. 자신감을 가지세요.",
        "어려운 일이 있을 수 있지만, 결국 해결될 것입니다. 희망을 가지세요.",
        "행운이 따라오는 하루입니다. 당신의 노력에 좋은 결과가 있을 것입니다.",
        "누군가의 도움을 받을 수 있는 기회가 생깁니다. 겸손하게 받아들이세요.",
        "오늘은 자신감을 가지고 주변 사람들과 소통을 강화하는 것이 좋습니다.",
        "건강을 챙기세요. 작은 변화가 큰 차이를 만들 수 있습니다.",
        "금전적으로 좋은 기회가 올 수 있습니다. 신중한 판단을 하세요.",
        "오늘은 휴식을 취하는 것도 중요합니다. 스트레스를 풀 수 있는 시간을 가지세요.",
        "새로운 계획을 세우기에 좋은 날입니다. 현실적으로 접근해 보세요.",
        "사소한 일에도 감사하는 마음을 가져보세요. 큰 행복이 따를 것입니다.",
        "일상에서 작은 기쁨을 찾아보세요. 그 속에서 큰 만족을 얻을 수 있습니다.",
        "오늘은 여행이나 외출이 좋은 기운을 불러올 수 있습니다. 새로운 경험을 해보세요.",
        "가족과의 시간이 행복을 가져올 것입니다. 함께하는 시간을 소중히 여세요.",
        "힘든 상황일수록 긍정적인 마음을 유지하세요. 그 자체가 좋은 결과를 불러올 것입니다.",
        "다소 불확실한 상황이라도, 마음을 비우고 편안한 마음을 가지세요.",
        # 부정적인 운세 추가
        "오늘은 예상치 못한 장애물이 생길 수 있습니다. 차분하게 대처하세요.",
        "현재의 상황이 조금 불안정할 수 있습니다. 너무 급하게 결정을 내리지 마세요.",
        "오늘은 계획이 예상대로 되지 않을 가능성이 큽니다. 유연하게 대처하세요.",
        "스트레스가 쌓일 수 있는 하루입니다. 잠시 휴식을 취하세요.",
        "주변의 사람들과 갈등이 생길 수 있으니, 감정을 잘 조절하는 것이 중요합니다.",
        "어떤 일에서 실패를 경험할 수 있습니다. 하지만 실패에서 배운 교훈을 소중히 여겨야 합니다.",
        "오늘은 신중한 판단이 중요한 날입니다. 직감보다는 이성적인 결정을 내리세요.",
        "기다리는 일이 더디게 진행될 수 있습니다. 인내심을 가지고 기다려야 할 때입니다.",
        "작은 실수로 인해 일이 꼬일 수 있습니다. 세심하게 주의를 기울이세요.",
        "다소 혼자의 시간이 필요할 수 있습니다. 스스로를 돌아보는 시간이 되어보세요."
    ]
    
    # 행운의 색깔 리스트 (영어 색상)
    lucky_colors = [
        "red", "blue", "green", "yellow", "magenta", "white", "black", "yellow", "cyan", "grey",
        "pink", "brown", "grey", "skyblue", "lightgreen", "turquoise", "purple", "peach", "orange", "lavender"
    ]
    
    # 행운의 색깔 한글 대응 리스트
    color_translation = {
        "red": "빨간색", "blue": "파란색", "green": "초록색", "yellow": "노란색", "magenta": "자홍색", 
        "white": "흰색", "black": "검은색", "cyan": "청록색", "grey": "회색", "pink": "핑크색", 
        "brown": "갈색", "skyblue": "하늘색", "lightgreen": "연두색", "turquoise": "청록색", 
        "purple": "보라색", "peach": "살구색", "orange": "주황색", "lavender": "라벤더색"
    }
    
    # 행운의 숫자 리스트 (1부터 60까지)
    lucky_numbers = list(range(1, 61))

    # 이니셜을 기준으로 고유한 인덱스를 생성 (이니셜을 숫자로 변환)
    initials_sum = sum(ord(c) for c in initials.lower())  # 이니셜을 소문자로 바꾸어 아스키 값 합산
    index = (initials_sum + sum(ord(c) for c in today_str)) % len(fortunes)

    # 운세, 색깔, 숫자 선택
    fortune = fortunes[index]
    lucky_color = lucky_colors[index % len(lucky_colors)]  # 색깔도 날짜와 이니셜에 맞춰 고르게
    lucky_number = lucky_numbers[index % len(lucky_numbers)]  # 숫자도 날짜와 이니셜에 맞춰 고르게

    # termcolor에서 지원되지 않는 색상 처리
    supported_colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white", "grey", "black"]
    if lucky_color not in supported_colors:
        lucky_color = "white"  # 지원되지 않는 색상은 기본 색상으로 처리

    # 한글로 변환된 색상
    lucky_color_korean = color_translation.get(lucky_color, "흰색")

    # 행운의 색깔을 적용한 운세 출력
    colored_fortune = colored(fortune, lucky_color)
    colored_lucky_color = colored(f"Lucky color: {lucky_color_korean}", lucky_color)

    return f"{today}의 운세: {colored_fortune}\n{colored_lucky_color}\n행운의 숫자: {lucky_number}"

# 이름의 이니셜 입력 받기
initials = input("이름의 이니셜을 입력하세요: ").strip()

# 운세 출력
print(get_daily_fortune(initials))
