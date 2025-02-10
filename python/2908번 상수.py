# https://www.acmicpc.net/problem/2908

n,m = input().split()

revers_n = n[::-1]
revers_m = m[::-1]

if revers_n > revers_m:
    print(revers_n)
else:
    print(revers_m)