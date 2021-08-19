fruits = {'apple', 'banana', 'orange'}

fruits.add('mongo')
print(fruits)

companies = set()
companies = {'apple', 'microsoft', 'google'}

# 교집합 
print(companies & fruits)

# 합집합 
print(companies | fruits)

# 집합끼리 뺴기 
print(companies - fruits)


# 연습문제 
dice1 = (1, 2, 3, 4, 5, 6)
dice2 = (2, 3, 5, 7, 11, 13)

def answer():
    for i in list(dice1):
        for j in list(dice2):
            print(i + j)

answer()

# 모법 답안 
sum_of_the_two_dice = set()
def good_answer():
    for x in dice1:
        for y in dice2:
            sum_of_the_two_dice.add(x + y)

print(sum_of_the_two_dice)