# 파이썬 자료형은 크게 number, sequence, mapping으로 나눌 수 있다.

# 숫자는 int, float, complex가 있다. 
print(type(3))
print(type(3.5))
print(type(3+4j))

# 시퀀스는 str, list, tuple이 속한다. 
# for문에서 사용할 수 있는 것들이 sequence들이다. 
print(type("love your enemis. for they tell you your faults"))
print(type(["live", "enemy", "fault"]))
print(type(('love', 'enemy', 'fault')))

# 문자열 슬라이싱 
p = "python"
print(p[:])
print(p[0:2])
print(p[:1])
print(p[::-1])
print(p[-2:])

# mapping
# mapping은 dictionary, set, bool이 있다. 
print(type({"jun": "good", "aa": "1111"}))
print(type(1 < 3))
print(type({"apple", 'banana'}))

# 문제 
# 거꾸로 배열해도 같은 단어 혹은 문장이 되는 것을(palindrome)이라고 한다. 

# Q1
# 주어진 단어가 회문인지 판별하는 함수 palindrome()을 작성하세요. 단, 문자열 입력은 모두 소문자로 이뤄지며 공백을 포함하지 않는다고 가정합니다.
def palindrome(str_):
    result = False 
    new_str = str_[::-1]
    if str_ == new_str:
        result = True
        
    return result

print(palindrome("str"))
print(palindrome("aaa"))
print(palindrome("banana"))

# 모법 답안 
def goodAnswer(s):
    s = s.lower()
    s = s.replace(' ', '')
    return s[:] == s[::-1]

if __name__ == '__main__':
    for x in ['anna', 'banana', 'anaa', 'my gg g']:
        if goodAnswer(x):
            print(f"'{x}' is a panlindrome")
        else:
            print(f"'{x}' is not a panlindrome")