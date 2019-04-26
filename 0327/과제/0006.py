numbers = list()
for i in range(4):
    numbers.append(int(input(str(i+1)+"번째 정수를 입력하십시오")))

print(numbers[0] + numbers[1] + numbers[2] + numbers[3])

''' Var. 1
n = 
numbers = list()
for i in range(n):
    numbers.append(int(input(str(i+1)+"번째 정수를 입력하십시오")))

numbersSum = 0
while(numbers != []):
    numbersSum += numbers.pop()

print(numbersSum)
'''