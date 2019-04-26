number = int(input("복권 번호를 입력하시오(0에서 99사이): "))

if number < 0 or number > 99:
    print("범위를 초과하였습니다.")
    exit(-1)

if number == 58:
    print("축하합니다.")
    print("복권에 당첨되셨습니다.")
else:
    print("유감입니다.")
    print("다음 기회를 이용해 주세요.")
    