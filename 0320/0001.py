ame = 2000 - 1200
latte = 3000 - 1900
cino = 3500 - 2100

ames = int(input("아메리카노 판매 개수: "))
lattes = int(input("카페라떼 판매 개수: "))
cinos = int(input("카푸치노 판매 개수: "))

sales = 0
sales += ame * ames
sales += latte * lattes
sales += cino * cinos

print("총 이익은",sales,"입니다.")