# https://www.acmicpc.net/problem/1769

num = input()
sum = 0
count = 0

while len(num) > 1:
    count += 1
    for i in range(len(num)):
        sum += int(num[i])
    num = str(sum)
    sum = 0

print(count)
if int(num) %3 == 0:
    print('YES')
else:
    print('NO')