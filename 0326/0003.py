birth = input("주민등록번호 앞 6자리를 입력하시오: ")

birth_y = birth[0:2]
birth_m = birth[2:4]
birth_d = birth[4:6]

print(f"당신은 {birth_y}년 {birth_m}월 {birth_d}일 생입니다.")