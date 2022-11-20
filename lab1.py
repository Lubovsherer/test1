# 1
a = 5
b = 12
c = (a ** 2 + b ** 2) ** 0.5
print(c)

#2
a = '1867'
print(a[-2])

#3
n = 15
print(n + 2 - (n % 2))

n = 14
print(n + 2 - (n % 2))

#4 -



#5
a = 16
b = 14

if a > b:
    print(1)
elif b > a:
    print(2)
else:
    print(0)

#6
a = 5
b = 7
c = 10

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)
else:
    print('-')

#7
column_number = 1
str_number = 1

column_number1 = 5
str_number1 = 1

if column_number == column_number1 or str_number == str_number1:
    print('yes')
else:
    print('no')

#8
a = 7
b = 24
c = 25
if (a+b) > c and (a+c) > b and (b+c) > a:
    print('yes')
else:
    print('no')

#9
a = 5
b = 5
c = 4
if a == b == c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
else:
    print(0)
#10
a = 9
b = 7
c = 11
if a <= b <= c:
    print(f'{a}, {b}, {c}')
elif a <= c <= b:
    print(f'{a}, {c}, {b}')
elif b <= a <= c:
    print(f'{b}, {a}, {c}')
elif b <= c <= a:
    print(f'{b}, {c}, {a}')
elif c <= a <= b:
    print(f'{c}, {a}, {b}')
elif c <= b <= a:
    print(f'{c}, {b}, {a}')
else:
    print("-")

#11 - нашла только как проверить остроугольные треугольники
# a = 6
# b = 6
# c = 6
# if ''' (a != b and a!=c and b!=c)
#         (a == b or a == c or b == c)
#         (a == b and a==c and b==c)''':
#      print('acute')
# elif:
#     print('impossible')