# find max muliplied number of card combinations

def max_product(left_cards, right_cards):
    sumList = list()
    for i in left_cards:
        for j in right_cards:
            sumList.append(i * j)
    return max(sumList)
    
# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))