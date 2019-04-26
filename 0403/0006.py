import random

correct = 0
prob = 0

while True:
    prob += 1
    
    a = random.randrange(100) + 1
    b = random.randrange(100) + 1
    
    #input(str(a) + " - " + str(b) + " = ? :")
    ans = input("%i> %i - %i = ? :" % (prob,a,b))
    
    # 답안을 입력하지 않았을 경우
    if ans == "":
        ans = 101 # 가능하지 않은 범위: 오답처리용
    else:ans = int(ans)
    
    if a-b == ans:
        correct += 1
        print(f"맞았습니다. ({correct}/{prob})")
    else:
        print(f"틀렸습니다. ({correct}/{prob})")