import time
now = time.time()
now_yr = int(1970 + now//(3600*24*365))
print("올해는",str(now_yr)+"년 입니다.")

age = int(input("몇 살이신지요? "))
print("2050년에는",str(age+2050-now_yr),"살 이시군요.")

print("당신이 몇 살 때 년도를 알고 싶습니까?")
toAge = int(input("입력> "))
print("당신이", str(toAge)+"살 때는", str(toAge-age + now_yr)+"년 입니다.")
