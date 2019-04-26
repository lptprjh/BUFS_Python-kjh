a = int(input("정수를 입력하시오 :"))
out = ""

while(a!=0):
  out = str(a % 2)+out
  a //= 2

print(out)