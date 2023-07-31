# 비트 AND 연산자 (&)
# : 각 비트를 비교해 모두 1이면 1을 반환, 그 외에는 0을 반환
a = 60 # 60 = 0011 1100
b = 13 # 13 = 0000 1101
print(a & b) # 0000 1100 (출력값 : 12)

# 비트 OR 연자사 (|)
# :  각 비트를 비교해 하나라도 1이면  1을 반환, 모두 0일 경우에만 0을 반환
print(a | b) # 0011 1101 (출력값 : 61)

# 비트 XOR 연산자 (^)
# : 각 비트를 비교해 서로 다르면 1을 반환, 같으면 0을 반환

# 비트 NOT 연산자 (~)
# : 각 비트르 반전

# 비트 왼쪽 시프트 연산자 (<<)
# : 비트 단위로 왼쪽으로 N비트 이동하면 2의 N 거듭제곱만큼 곱셈
a = 60
print(a << 2)

# 비트 오른쪽 시프르 연산자 (>>)
# : 비트 단위로 오른쪽으로 N비트 이동하면 2의 N 거듭제곱만큼 나눗셈
a = 60
print(a >> 2)

### 시퀀스 연산자 ###
# : 시퀀스(sequence) : 데이터의 순차적인 나열을 의미
# ex) 리스트, 튜플, 문자열 등

# 결합 연산자 (+)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)

# 복제 연산자 (*)
print(list1 * 3)

### 기타 연산자 ###
# 멤버십 연산자
# : 어떤 값이 지정된 컬렉션에 포함되어 있는지 확인하는 데 사용

list = [1, 2, 3, 4, 5]
str = "Hello, Python"

# in 연산자
# : 시퀀스나 컬렉션에 특정 요소가 포함되어 있으면 True
# : 그렇지 않으면 False를 반환
print(3 in list) # True
print(6 in list) # False

print('Python' in str) # True
print('World' in str) # False

# not in 연산자
# : 시퀀스나 컬렉션에 특정 요소가 포함되어 있지 않으면 True
# : 포함되어 있지 않으면 False를 반환
print(3 not in list) # False
print(6 not in list) # True

print('Python' not in str) # False
print('World' not in str) # True

### 연산자의 우선순위 ###
# 1. 괄호 ()
# 2. 지수 연산자 **
# 3. 부호 연산자(양수, 음수) +x, -y

# 4. 곱셈, 나눗셈, 나머지, 몫
# 5. 덧셈, 뺄셈