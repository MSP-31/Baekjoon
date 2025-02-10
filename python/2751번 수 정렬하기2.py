# https://www.acmicpc.net/problem/2751
# 시간초과 문제로 인하여 input을 sys.stdin.readline()로 교체함
import sys

num = []

count = int(sys.stdin.readline())

for i in range(count):
    num.append(int(sys.stdin.readline()))

num.sort()

for i in range(count):
    print(num[i])