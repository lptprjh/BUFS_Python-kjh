Oniichan = open("filename.txt",'r')
Daisuki = Oniichan.readlines()
for i in range(len(Daisuki)):
    Daisuki[i] = Daisuki[i].rstrip()
print(Daisuki)
Oniichan.close()

# 한줄로 요약
with open("filename.txt",'r') as yandered:print(list(map(str.rstrip,yandered.readlines())))
