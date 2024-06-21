# https://www.acmicpc.net/problem/1259

result = []

while True:
    i = input()
    if i == '0':
        break
    elif i == i[::-1]:
        result.append('yes')
    else:
        result.append('no')

for i in result:
    print(i)