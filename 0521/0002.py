a = list()
for i in range(20):
    a.append(i+1)

offset = 0
while offset < len(a):
    asdf = a[offset]
    if asdf%2==0 or asdf%3==0:
        a.pop(offset)
    else: offset += 1

print(a)