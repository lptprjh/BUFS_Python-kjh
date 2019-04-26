score = int(input("점수를 입력 :"))

if score >= 90                : rank = "A"
if score >= 80 and score < 90 : rank = "B"
if score >= 70 and score < 80 : rank = "C"
if score >= 60 and score < 70 : rank = "D"
if                 score < 60 : rank = "F"

print(rank)