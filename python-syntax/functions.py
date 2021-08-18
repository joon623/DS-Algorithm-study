def print_list(a):
  for i in range(0,a):
    print(i)
print_list(5)

# 연습 문제 구구단
def multipy():
  for i in range(2, 10):
    for j in range(2, 10):
      print(i * j)    
multipy()

# 반환문 
def f1(x):
  a = 3
  b = 5
  y = a * x + b
  return y  
c = f1(10)
print(c)

# 지역 변수, 전역 변수
x = 100
def printx():
    print("x:",x)
printx()

# 함수 안에서 전역변수 만들기 
# 함수 안에서 전역 변수를 만든다..?
def e_is_10():
    global e 
    e = 10
    print('e 값은 ', e)

e_is_10()
print(e)

# 람다(lambda)
def hap(x, y):
    print(x + y)
    return x + y

hap(10, 20)
aa = (lambda x,y: x + y)(10,20)
print(aa)
print( type(range(5)))
# map 함수 
# map(함수, 리스트)
