# https://www.acmicpc.net/problem/18870

# 빈 딕셔너리
result = {}

num = int(input())
x = list(map(int,input().split()))

# set으로 변환해서 중복 제거
sorted_x = list(set(x))

# 순서 정렬
sorted_x = sorted(sorted_x)

# 딕셔너리에 키-값 쌍 추가
for i in range(len(sorted_x)):
    result[sorted_x[i]] = i

# x[i]와 result의 키와 일치하면 result의 값으로 덮어씌움
for i, value in enumerate(x):
    x[i] = result.get(value,value)

for i in range(num):
    print(x[i],end=" ")