# 책: p.199
def vending_machine(money):
    # 음료수 가격
    drink_price = 700

    # 음료수 개수 & 잔돈 계산
    num_drink = money // drink_price # 돈을 음료수 가격으로 나눈 몫이 윰료수 개수
    change = money % drink_price # 돈을 음료수 가격으로 나눈 나머지가 잔돈

    # 출력
    print(f'{money}원을 넣었을 때: {num_drink}잔의 음료수, 잔돈 {change}')

vending_machine(3000)

# 1.
def hello_world():
    print('Hello, World!')
hello_world()

# 2.

# 3.
def sum_numbers(numbers):
    return sum(numbers)
print(sum_numbers([1, 2, 3, 4, 5]))

# 4.
def greet(name='Guest'):
    print(f'Hello, {name}')
greet('Yemin')
greet()

# 가변 인자(매개변수)를 받아 평균을 반환하는 함수를 작성

def average(*args):
    return sum(args) / len(args)

print(average(1, 2, 3, 4, 5))