class Sports:

    def running(self):
        print("sports")

class Badminton(Sports):

    def __init__(self):
        self.state = False
        self.veriation = []
    
    def defence(self):
        print("수비를 하는 중입니다.")
    
    def attack(self):
        print("공격을 하는 중입니다.")


badminton = Badminton()
badminton.attack()
badminton.defence()
badminton.running()
print(badminton.state)
print(badminton.veriation)


# __name__ 변수란 ?
# 파이썬의 내부적으로 사용하는 특별한 변수 이름이다. 

# 특별한 메소드들
class Book:
    area = 11

    def setData(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

    def printData(self):
        print("제목 : ", self.title)
        print("제목 : ", self.price)
        print("제목 : ", self.author)

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        print("책 객체를 새로 만들었어요.")

    def __del__(self):
        print("del 메서드")

    def __repr__(self):
        return self.title
    
    def __add__(self, other):
        return self.area + other

#  __init__ 메서드는 어떤 클래스의 객체가 만들어질 때 자동으로 호출되어서 그 객체가 갖게 될 여러 가지 성질을 정해주는 일을 한다. 
# __del__ 메서드는 객체가 없어질 때 호출되는 메서드이다. 이런것을 destructor라고 한다.
#  repr 메서드는 문자열을 return 한다.

book = Book(1,2,3)
print(book.__add__(202))