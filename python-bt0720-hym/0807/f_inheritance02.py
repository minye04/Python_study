# 학생 - 사람의 클래를 상속관계로 구형 #

# super()함수
# : 자식 클래스에서 부모 클래스의 메서드나 속성에 접근하기 위해 사용

class Person: # 슈퍼 클래스

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(self.name + '가' + food + '를 먹습니다.')

class Student(Person): # 서브 클래스

    def __init__(self, name, school):
        super().__init__(name) # 부모 클래스의 __init__ 메서드 호춣
        self.school = school

    def study(self):
        print(self.name + '는' + self.school + '에서 공부합니다.')

yemin = Student('황예민', '코리아IT아카데미')
yemin.eat('아이스크림')
yemin.study()

junGook = Person('이준국')
junGook.eat('초콜릿')