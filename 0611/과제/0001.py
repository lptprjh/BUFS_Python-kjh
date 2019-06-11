with open('data.txt','r') as m:
    # 앞서 파일을 m으로 불러들인 다음,
    # m에 있는 파일을 행별로 끊어 리스트로 불러오고,
    # 그 리스트 항목 하나하나에 대해 str.rstrip()을 실행해 개행문자를 지우고,
    # 그 뒤에 문자열을 float로 변환하는 작업을 거치고,
    # 그 최종결과는 map object이므로 그대로 사용하기엔 애로사항이 꽃핌.
    # 따라서 list로 변환.
    n = list(map(float,map(str.rstrip,m.readlines())))
    print(sum(n)/len(n))
    
'''### Alt.1 지금까지 배운 내용을 위주로
f = open('data.txt','r') #파일을 읽어온다

a = f.readlines().rstrip() #파일에서 문자열을 행별로 불러오고, 개행문자를 잘라낸다

# 리스트 안에 저장된 숫자는 모두 문자열이므로, 이를 숫자열로 바꾸는 작업이 필요하다.
b = list()
for n in a:
    b.append(float(n))

# 평균을 출력
print(sum(b) / len(b))

# 메모리 누수 방지를 위해 파일을 닫아 줍니다
f.close()
'''
