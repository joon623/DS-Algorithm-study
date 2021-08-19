# 튜플은 리스트와 비슷한 역할을 하는 자료형이다. 
# 두 변수의 값을 바꾸기 위해서 변수 하나를 더 만들어야 한다. 
a = 10 
b = 20 
temp = a
a = b 
b = temp 
print(a, b)

# 파이썬에서는 간단하게 바꿀 수 있다. 
c = 10 
d = 20 
c, d = d, c
print(c, d)

# 인자에 *를 붙여두면 그 이후에 들어오는 것은 모두 튜플ㅇ에 집어 넣는다. 
def magu_print(x, y, *rest):
    print(x, y, rest)
    return x, y, rest

print(magu_print(1, 2, 3))
print(magu_print(1, 2, 3, 5, 6, 7, 9, 10))

# 원소가 없는 튜플은 꼭 ()를 써줘야 한다. 
empty = ()
one = 5,
pp = (1, 2, 3)
qq = list(pp)