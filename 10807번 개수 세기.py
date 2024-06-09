# https://www.acmicpc.net/problem/10807

n = int(input())
nums = list(map(int,input().split()))
v = int(input())

a = sum(i == v for i in nums)
print(a)