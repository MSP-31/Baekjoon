# https://www.acmicpc.net/problem/28018
# 배열 크기가 작아서 index에러가 났었음
import sys

n = int(sys.stdin.readline())

time = [0] * n
for i in range(n):
    s,e = map(int,sys.stdin.readline().split())
    time[i] = [s,e]

q = int(sys.stdin.readline())
time_q = list(map(int,sys.stdin.readline().split()))

# 누적합 배열 초기화
cumulative = [0] * 1000002

# 1은 시작 -1 은 끝을 표시함
for s,e in time:
    cumulative[s] += 1
    cumulative[e+1] -= 1

# 1부터 시작해서 이전값을 더해 누적합 계산
for i in range(1,len(cumulative)):
    cumulative[i] += cumulative[i - 1]

for i in time_q:
    print(cumulative[i])
