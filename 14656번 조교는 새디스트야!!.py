# https://www.acmicpc.net/problem/14656

num = int(input())

# 공백으로 구분하여 정수형 리스트로 입력받음
x = list(map(int,input().split()))
count = 0

for i in range(num):
    # 순서가 다르다면 카운트
    if (i+1) != x[i]:
        count += 1

print(count)