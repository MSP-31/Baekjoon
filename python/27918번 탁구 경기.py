# https://www.acmicpc.net/problem/27918

x = 0
y = 0

n = int(input())

for i in range(n):
    s = input()
    
    # 절대값으로 비교해서 2보다 크거나 같지않다면
    if not abs(x - y) >= 2:
        if s == 'D':
            x += 1
        elif s == 'P':
            y += 1
    
print(x,':',y,sep='')