Oniichan = open("filename.txt",'r')
Daisuki = Oniichan.read() # 파일 하나를 통채로 string 형식으로 복사
#Oniichan.readline()  # 한 줄을 string으로 (\n 불포함)
#Oniichan.readlines() # 개행 단위로 항목을 나누어 list로 복사 (\n 포함, .rstrip()으로 정리)
print(Daisuki)
Oniichan.close()
