# https://www.acmicpc.net/problem/27959

money, choco= map(int,input().split())

money *= 100

if money >= choco:
    print("Yes")
else:
    print("No")