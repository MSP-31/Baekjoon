# https://www.acmicpc.net/problem/1157

alp = [0] * 26
count = 0

text = list(input().upper())

# 알파벳의 해당하는 위치에 +1
for i in text:
    alp[ord(i)-65] += 1

for i in range(len(alp)):
    if alp[i] == max(alp):
        count += 1
    else:
        continue

if count == 1:
    result = chr(alp.index(max(alp)) + 65)
    print(result)
else:
    print("?")
    