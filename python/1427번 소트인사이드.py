# https://www.acmicpc.net/problem/1427

n = input()
# 문자열 정렬
nr = sorted(n,reverse=True)
# 문자열을 하나로 합치고 정수형으로 바꿈
nr = int(''.join(nr))

print(nr)