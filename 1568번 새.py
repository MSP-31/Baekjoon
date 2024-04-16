# https://www.acmicpc.net/problem/1568

n = int(input())
sing = 1
count = 0

# n이 0보다 크면 반복
while(n > 0):
    # sing 이 n보다 크다면 sing 초기화
    if n < sing:
        sing = 1
    n -= sing
    
    count += 1
    sing += 1

print(count)