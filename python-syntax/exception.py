def foo(a,b):
    try:
        if a and b:
            return a / b
        elif a:
            return "elif"
        else:
            return "먼가 이상해"
    except:
        return "똑바로 해라"

print(foo(2, 3))
print(foo(2, 0))
print(foo(2, 2))

def foo2(a,b):
    try:
        return a / b
    except:
        return "먼가 잘못됐어"

print(foo2(1,0))