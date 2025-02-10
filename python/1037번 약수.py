# https://www.acmicpc.net/problem/1037

n = int(input())
nums = list(map(int,input().split()))
# n = max(nums) * min(nums)
print(max(nums)*min(nums))
