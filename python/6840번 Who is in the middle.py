# https://www.acmicpc.net/problem/6840

n = []

for i in range(3):
    n.append(int(input()))

n.sort()
print(n[1])