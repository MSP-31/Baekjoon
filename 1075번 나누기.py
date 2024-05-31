# https://www.acmicpc.net/problem/1075

n = input()
n = n[:-2]
n = int(n + '00')

f = int(input())

while 1:
    if n % f:
        n += 1
    else:
        break

print(str(n)[-2:])
