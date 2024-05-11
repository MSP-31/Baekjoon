# https://www.acmicpc.net/problem/25305

n,k = map(int,input().split())
x = list(map(int,input().split()))

x.sort(reverse=True)
print(x[k-1])