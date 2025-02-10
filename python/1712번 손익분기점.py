# https://www.acmicpc.net/problem/1712

fix, var, cost = map(int,input().split())

# 손익분기점을 넘길수 없음
if cost <= var:
    print(-1)
else:
    print(fix//(cost-var)+1)