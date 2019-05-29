a = list()

for i in range(5):
    a.append(float(input()))

summ = 0
for i in a: summ += i
print(summ/len(a))