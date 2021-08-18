# 변수 선언 
watch = 10000
lightter = 100
print(watch + lightter)

# 문자열 변수 
a = "pig"
b = "dad"
print(a + b)

# 리스트(list)
family = ['mother', 'father', 'gentleman', 'sexy lady']
for x in family: 
    print(x)

print(len(family)) # len 함수는 리스트의 원소가 몇 개 들었는지 보여준다. 
print(family[3])
family.remove("gentleman")
print(family)

# 인터 프리터와 컴파일러
# 고급 언어를 컴퓨터가 알아들을 수 있게 번역을 해줄 필요가 있다. 
# 인터프리터는 한 마디 할 떄마다 통역을 하는 것이고 컴파일은 처음부터 끝까지 듣고 나서 한번에 바꿔주는 것을 말한다. 
# 파이썬은 인터프리터 언어이다.


# 연습 문제 정수를 입력받고 
answer = int(input("정수를 입력하시오."))
print(answer ** 2)

# while을 사용하는 반복문
num = 1
while num <= 100:
    print(num)
    num = num + 1  

# 문제
# 정수를 한 개 입력받아, 1부터 입력받은 수까지 각각에 대해 제곱을 구해 프린트하는 프로그램을 작성해 보세요. 단, while 문을 사용하세요.

current = 1
answer_2 = int(input("정수를 입력 받아"))    
while current <= answer_2:
    print(current ** 2)
    current += 1

# 조건문 if-elif-else
a__ = 1234 * 4
b__ = 13456 / 2

if a > b:
    print("a > b")
elif a == b:
    print(" a == b")
else:
    print("b > a")



# 조건문에 따라 반복문 중단하기
max_ = 10;
while True:
    num = int(input("조건문에 따라 반복문 중단하기"))
    if num > max_: 
        print(num, "num str(num)")
        break

# range 함수 
a__ = [1, 15, 20, 11111111]
for i in a__:
    print(i)

for i in range(5, 10):
    print(i)

# 연습 문제 제곱표 (for)
z__ = int(input("정수를 입력하세여"))
for i in range(1, z__):
    print(i ** 2)