a = 0
n = 5 # 몇 개의 숫자의 평균을 구할 것인가?

for i in range(n): # n=5 ⇒ i = 0,1,2,3,4
    a += int(input(i+1,"번째 숫자를 입력하십시오: "))
print("평균:",a/n)

''' Variation 1
a += int(input("1번째 숫자를 입력하십시오: "))
b += int(input("2번째 숫자를 입력하십시오: "))
c += int(input("3번째 숫자를 입력하십시오: "))
d += int(input("4번째 숫자를 입력하십시오: "))
e += int(input("5번째 숫자를 입력하십시오: "))
print("평균:", (a+b+c+d+e)/5)
''' 

''' Variation 2
print("평균:", (
    int(input("1번째 숫자를 입력하십시오: "))+
    int(input("2번째 숫자를 입력하십시오: "))+
    int(input("3번째 숫자를 입력하십시오: "))+
    int(input("4번째 숫자를 입력하십시오: "))+
    int(input("5번째 숫자를 입력하십시오: "))
    ) /5 )
'''