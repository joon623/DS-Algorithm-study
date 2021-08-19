
class Singer:
    def sing(self):
        return "Lalala"

taeji = Singer()
print(taeji.sing())

class Amazon:
    stregth = 20
    dexterity = 25

    def attack(self):
        return 'job!!'

# self라는 것은 그 클래스의 객체를 가리킨다. 


class Person:
     # 눈 두 개, 코 하나, 입 하나...
    eyes = 2
    nose = 1
    mouth = 1
    ears = 2
    arms = 2
    legs = 2

    # 먹고 자고 이야기하고...
    def eat(self):
        print('얌냠...')

    def sleep(self):
        print('쿨쿨...')

    def talk(self):
        print('주절주절...')

class Student(Person):
    def study(self):
        print("열공 열공..")

lee = Person()
aaaaa = lee.mouth
print(aaaaa)
print(lee.sleep())

class Fridge: 
    def __init__(self):
        self.isOpened = False
        self.foods = []

    def open(self):
        self.isOpened = True
        print("냉장고 문을 열었어요")

    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)
            print("냉장고 속에 음식이 들어갔네..")
        else:
            print("냉장고 문이 닫혀있어서 못넣겠다.")

    def close(self):
        self.isOpened = False
        print("냉장고 문을 닫았어요>>")
    
# 클래스에 쓸 내용이 없으면 pass라고 쓰면 된다.
class Food:
    pass