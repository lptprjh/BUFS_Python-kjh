class Money:
    def __init__(self,money=0):
        self.money = money

    # 잔액 충전 (반환: 충전 후 잔액)
    def add(self, a):
        self.money += a
        return self.money
    
    # 잔액을 이용하여 결제 (반환: 결제 후 잔액. 결제 실패 시 -1)
    def pay(self, price):
        if price > self.money:
            return -1
        else:
            self.money -= price
            return self.money
    
    # 현재 잔액으로 결제할 수 있는지 확인 (결제할 수 있는 경우 True, 인수가 없는 경우엔 잔액 유무)
    def available(self, price=1):
        if price > self.money:
            return False
        else:
            return True
    
    # 거스름돈 반환
    def Return(self):
        R = [0,0,0,0] #500원, 100원, 50원, 10원

        R[0] = self.money // 500
        self.pay(R[0]*500)
        R[1] = self.money // 100
        self.pay(R[1]*100)
        R[2] = self.money // 50
        self.pay(R[2]*50)
        R[3] = self.money // 10
        self.pay(R[3]*10)

        return R


money = Money(int(input("투입한 돈: ")))
price = int(input("물건 값: "))

if not money.available(price):
    print("잔액이 부족합니다.",price-money.money,"원을 더 투입하여 주십시오.")
    exit(-1)

money.pay(price)
print("거스름돈: ", money.money)

Return = money.Return()

print("500원 동전의 갯수:", Return[0])
print("100원 동전의 갯수:", Return[1])
print("50원 동전의 갯수:", Return[2])
print("10원 동전의 갯수:", Return[3])

if money.money is not 0:
    print("10원 미만 금액 ",money.money,"원은 반환되지 않았습니다.",sep='')