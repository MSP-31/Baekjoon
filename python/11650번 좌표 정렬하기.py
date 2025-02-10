# https://www.acmicpc.net/problem/11650
# lambda는 의미 익명함수를 지칭하는 용어 즉, 기존의 함수(명 등)을 선언하고 사용하던 방식과는 달리 바로 정의하여 사용할 수 있는 함수.

n = int(input())
points = []

# 좌표 입력받음
for i in range(n):
    x,y = map(int,input().split())
    points.append((x,y))

# 첫번째 요소, 두번째 요소를 기준으로 정렬
sorted_points = sorted(points, key=lambda x: (x[0],x[1]))

# 형식을 x y 로 바꿈
resutl = [f"{x} {y}" for x,y in sorted_points]

for i in resutl:
    print(i)