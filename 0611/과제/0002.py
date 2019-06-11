with open('input.txt','r') as f:
    l = list(map(str.rstrip,map(str.lstrip,f.read().split())))
    print(l)
    print(len(l))
