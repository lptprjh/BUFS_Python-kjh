a = list()
for i in range(20):
    a.append(i+1)

offset = 0
while offset < len(a):
    asdf = a[offset]
    if asdf%2==0 or asdf%3==0:
        del a[offset]
    else: offset += 1

print(a)

''' Var.1 생성할 때부터 걸러내기
a = list()
for i in range(20):
    if not (i%2==0 or i%3==0):
        a.append(i+1)

print(a)
'''