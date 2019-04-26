#[a,b]일때, a단에서 b단까지 출력합니다.
danRange = [8,9] 

b = 1
while b <= 9:
    for a in range(danRange[0], danRange[1]+1):
        print("%2i × %2i = %3i" % (a,b,a*b), end=' | ')
    print()
    b += 1