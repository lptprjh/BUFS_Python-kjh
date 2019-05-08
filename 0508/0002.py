def get_sum(start,end,inc):
    out = 0
    for i in range(start,end+1,inc):
        out += i
    return out

print(get_sum(1,10,2))