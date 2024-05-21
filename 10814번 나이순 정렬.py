# https://www.acmicpc.net/problem/10814

num = int(input())
n = []

for i in range(num):
    age, name = input().split()
    age = int(age)
    # 순서도 같이 저장
    n.append([age,name,i])

# 나이순으로 정렬후에 순서순으로 한번더 정렬
sorted_n = sorted(n, key=lambda x: (x[0],x[2]))

# 형식을 x y 로 바꿈
resutl = [f"{x} {y}" for x,y,_ in sorted_n]

for i in resutl:
    print(i)