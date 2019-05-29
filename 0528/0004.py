# list().sort() 사용하지 않고 합병 정렬(Merge sort)을 이용하여 정렬하기
def mergesort(lst=list()):
    half = int(len(lst)/2)

    if len(lst) > 1:
        out = list()
        L = mergesort(lst[:half])
        R = mergesort(lst[half:])
        
        while len(L)>0 and len(R)>0:
            if L[0] > R[0]:
                out.append(R.pop(0))
            else:
                out.append(L.pop(0))
        while len(L) != 0: out.append(L.pop(0))
        while len(R) != 0: out.append(R.pop(0))
        
        return out
    else:
        return lst

lst = [28, 12, 9, 32, 25, 8, 16, 23, 5, 17, 19, 11]
print(mergesort(lst))