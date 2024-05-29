# https://www.acmicpc.net/problem/2745
result = 0

inp = list(input().split())

format = int(inp[1])
num = list(inp[0])
num.reverse() # 역순

for i in range(len(num)):
    f = format ** i
    if str.isalpha(num[i]):
        # 문자를 아스키코드로 변환한 다음 숫자로 바꿈
        n = ord(num[i].upper()) - 55
        result += n * f
    else:
        result += int(num[i]) * f

print(result)