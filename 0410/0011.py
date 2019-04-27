n = int(input("정수를 입력하시오: "))

sum = 0
for i in range(n):
    sum += i+1

print(sum)
    
''' Var 1. 치사한 짓거리: 등차수열의 합 공식 이용
print(n*(1+n)/2)
'''

''' Var 2. 재귀함수
def ad(n):
    if n <= 0: return n
    else: return n + fact(n-1)

print(ad(n))
'''