# https://www.acmicpc.net/problem/10989
# 시간초과 문제로 인하여 input을 sys.stdin.readline()로 교체함
# 계수정렬 활용
import sys

num = int(sys.stdin.readline())
count = [0] * 10001

for _ in range(num):
    temp = (int(sys.stdin.readline()))
    # 각 원소가 몇번 나오는지 기록
    count[temp] += 1

for i in range(len(count)):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)