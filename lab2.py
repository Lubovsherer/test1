#1 - тут я не знаю, как сделать их в одну строку
a = int(input())
b = int(input())

for numbers in range(a, b+1, 2):
    print(numbers)

#2
x = int(input('x='))

for i in range(2, x+1):
    if x % i == 0:
        print(i)
        break

#3
x = int(input('x='))

for i in range(1, x+1):
    if x % i == 0:
        print(i, end= '')

#4
N = int(input('sum='))
sum = 0

for i in range(0, N):
    sum += int(input())
    print(sum)

