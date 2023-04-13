a = int(input())

b = a // 1000

x = b // 100
y = b // 10 % 10
z = b % 10

c = a % 1000

k = c // 100
l = c // 10 % 10
m = c % 10

if (x + y + z) == (k + l + m):
    print('YES')
else:
    print('NO')
    