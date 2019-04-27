import random

options=["왼쪽 상단", "왼쪽 하단", "중앙", "오른쪽 상단", "오른쪽 하단"]
computer_choice = random.choice(options)


print("어디를 수비하시겠어요? (", end='')
for pos in options:
	print(pos, end='')
	if not pos==options[-1]:
		print(', ', end='')
	else:
		print(')')

user_choice = input("입력>")

if computer_choice == user_choice:
	print("수비에 성공하셨습니다.")
else:
	print("패널티 킥이 성공하였습니다.")