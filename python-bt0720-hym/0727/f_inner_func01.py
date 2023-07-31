### 내장 함수 (Built-in Function)

# 내장 함수: 파이썬(프로그램)이 기본적으로 제공하는 함수
#           별도의 라이브러리나 모듈을 불러오지 않고도 사용 가능(import 하지 않아도 사용 가능)
# 교과서 p.146

# 문자열 내장 함수

# 1. chr() 함수
# : 문자 자신만이 가지는 코드 값(문자 코드 - 유니코드)를 반환
# : 문자 코드에는 미국 표준 코드(아스키코드), 국제 표준 코드(유니 코드) 등이 있다.

print(chr(65))
print(chr(97))

# 2. ord() 함수
# : 문자를 전달하면 해당 문자의 유니코드 값을 반환

print(ord('A'))
print(ord('a'))

# 3. eval() 함수
# : 실행하고자 하는 표현식을 문자열로 전달하면 표현식의 결괏값을 반환

print(eval('100+200'))

a = 10
print(eval(' a * 5'))

# format() 함수
# : 전달받은 인수와 포맷 코드에 따라 형식을 갖춘 문자열을 반환

print(format(10000)) # 숫자형 10000이 문자형 '10000'으로 출력
print(format(10000, ',')) # 숫자를 천 단위로 표현할 때 사용

# str() 함수
# : 전달받은 값을 문자열로 반환

print(str(10))
print(str(1.5))