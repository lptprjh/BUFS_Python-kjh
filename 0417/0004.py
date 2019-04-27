total = 0
i = -1
while i != 0:
    try: i = int(input("숫자를 입력하세요: "))
    # 빈 줄/문자열 등 정수로 변환할 수 없는 값을 입력할 경우에도 0을 입력한 것과 같은 효과를 냄
    except ValueError: break
    
    if i>0: total += i

print(total)