# https://www.acmicpc.net/problem/1002

import math

result = []

num = int(input())

for i in range(num):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())

    # 좌표 평면에서 두 원 사이의 거리
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    r_sum = r1 + r2
    r_abs = abs(r1-r2)

    # 두 원이 완전히 같을때
    if x1 == x2 and y1 == y2 and r1 == r2:
        result.append(-1)
    else:
        # 두 원이 서로 겹치지 않음
        if d > r_sum:
            result.append(0)

        # 두 원이 서로 외접함
        if d == r_sum:
            result.append(1)

        # 두 원이 겹침
        if r_abs < d < r_sum:
            result.append(2)
    
        # 두 원이 내접함
        if d == r_abs:
            result.append(1)
    
        # 한 원이 다른 원안에 있음
        if d < r_abs:
            result.append(0)

for i in result:
    print(i)