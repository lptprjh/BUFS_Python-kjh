#확장성을 고려한 설계 - 경매에 참가한 사람 모두를 정렬
def Haekshim(lst):
    # 연번(0부터 시작)
    order = list(range(len(lst)))
    sorted = False

    # 주어진 리스트의 정렬이 완료될 때 까지 반복
    while sorted is False:
        sorted = True
        for i in range(len(lst)-1):    
            # 순서가 어긋난 부분을 발견할 시
            if lst[i] > lst[i+1]:
                # 리스트가 정렬되어 있지 않았음을 표시
                sorted = False
                # 어긋난 순서를 바로잡음
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
                # 연번도 수정
                temp = order[i]
                order[i] = order[i+1]
                order[i+1] = temp
            
            # 순서는 같으나 연번이 정렬되지 않은 경우
            if lst[i] == lst[i+1] and order[i] > order[i+1]:
                temp = order[i]
                order[i] = order[i+1]
                order[i+1] = temp
    #정렬된 숫자와 연번을 튜플로 반환
    return (lst, order)

Gyeongmae = list()
for i in range(10):
    Gyeongmae.append(int(input()))

Gyeongmae = Haekshim(Gyeongmae)
# 입찰가가 모두 다르다는 조건에 따라
second = Gyeongmae[1][-2] + 1
print(second)

'''
def bubblesort(lst):
    sorted = False
    #Loop for sorting
    while sorted is False:
        sorted = True
        for i in range(len(lst)-1):    
            #If it find the list is not sorted
            if lst[i] > lst[i+1]:
                #Flag the list is not sorted
                sorted = False
                #Change two of them
                temp = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = temp
    #Return the sorted list
    return lst
'''