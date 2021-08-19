# String
x = "banana"
print(x[0])
print(x[2:4])
print(x[:3])
print(x[3:])

s = "hello python"
print(s.find("3"))
print(s.split(" ")[0])


# 파이썬 crud append, remove
prime = [3, 6, 11]
print(prime)
prime.append(5)
print(prime)
prime.insert(1, 2)
print(prime)
del prime[3]
print(prime)
prime.pop()
print(prime)
prime[0] = 10101010
print(prime)
prime.sort()
print(prime)

# list in list 
orders = ['potato', ['pizza', 'coke', 'salad'], 'hamburger']
print(orders[1][2])

# list로 행렬 표현 
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

one_to_ten = list(range(1, 10))
print(one_to_ten)

# 연습문제 
# 정수 num을 매개변수로 받아 각 자리 숫자(digit)의 합을 계산하는 sumOfDigits() 함수를 작성하세요. 단, 나눗셈을 이용하지 말고 풀어보세요.
def sum_of_digits(num):
    num_ = str(num)
    result = 0
    for i in range(len(num_)):
        result += int(num_[i])
    return result 

print(sum_of_digits(234))


def good_answer(num):
    sum = 0
    for c in list(str(num)):
        sum += int(c)
    return sum
    
print(good_answer(123))

print(list(str(333333)))
print(list("1o238u1923"))