# https://www.acmicpc.net/problem/11005
result = []

n,b = map(int,input().split())

# n이 0이 될때까지 반복
while n:
    # num 은 n을 b로 나눈 나머지값
    num = n%b
    if num < 10:
        result.append(num)
    else:
        # +55를 더해서 알파벳으로 변환
        result.append(chr(num + 55))
    # n을 b로 나눈 몫을 계속 저장
    n //= b

length = len(result)
for i in range(length):
    print(result[(length-1)-i],end="")