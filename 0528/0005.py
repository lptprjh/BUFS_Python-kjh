import random

def solve(prob):
    a = prob[0]
    b = prob[2]
    if prob[1] == "+": return a + b
    if prob[1] == "-": return a - b
    if prob[1] == "*": return a * b
    else:return None

probs = list()
probs.append((3,"+",5))
probs.append((8,"+",5))
probs.append((100,"-",5))
probs.append((23,"-",5))
probs.append((7,"*",7))

prob = random.choice(probs)
ans = int(input( "%i %s %i = "%prob ))
if ans == solve(prob): print("맞았습니다!")
else: print("틀렸습니다! (입력:%3i, 정답:%3i)" % (ans, solve(prob)) )