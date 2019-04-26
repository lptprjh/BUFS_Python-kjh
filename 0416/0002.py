result = 0

for i in range(100,200+1,2):
    if i%2 != 0: #홀수일 경우
        result += i

print(result)