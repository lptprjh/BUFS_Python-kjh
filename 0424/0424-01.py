#간결한 설계 - 경매에 참가한 사람 중 1,2위만 기록
Gyeongmae = list()
for i in range(10):
    Gyeongmae.append(int(input()))

Highst = [0,0] #금액, 연번
Second = [0,0]
for Saram in range(len(Gyeongmae)):
    #최고가 경신시
    if Gyeongmae[Saram] > Highst[0]:
        Second = Highst
        Highst = [Gyeongmae[Saram], Saram]
    #최고가는 아니지만 두 번째보단 클 경우
    elif Gyeongmae[Saram] > Second[0]:
        Second = [Gyeongmae[Saram], Saram]

print(Second[1]+1)