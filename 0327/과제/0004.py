print("안녕하세요?")
name = input("이름이 어떻게 되시나요?")

print("만나서 반갑습니다." + name + "씨")
print("이름의 길이는 다음과 같군요:", end="")
print(len(name))

age = int(input("나이가 어떻게 되시나요? "))
print("내년이면", str(age+1), "살이 되시는군요.")

hobby = input("취미가 무엇인가요? ")
print("네, 저도",hobby,"좋아합니다.")