#재귀함수 응용
def SumToZeroFrom(n):
    if n==0:
        return 0
    elif n<0:
        return n + SumToZeroFrom(n+1)
    elif n>0:
        return n + SumToZeroFrom(n-1)

print(SumToZeroFrom(int(input("정수를 입력하시오: "))))

''' 정석
number = int(input("정수를 입력하시오: "))
out = 0

for i in range(1,number+1):
    out += i

print(out)
'''

'''치사한 짓거리 (등차수열의 합)
def Sum(n1):
    return n*(n+1)/2
'''