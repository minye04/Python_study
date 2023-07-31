# 1.
num = 15

if num > 0:
    print('양수입니다')
else:
    if num < 0:
        print('음수입니다')
    else:
        print('0입니다')

# 2.
total = 0
for i in range(1, 11):
    total += i # total = total + i
print('The sum from 1 to 10 is', total)

