# https://www.acmicpc.net/problem/17826

score = list(map(int,input().split()))
num = int(input())

if num >= score[4]: print("A+")
elif num <= score[5] and num >= score[14]: print("A0")
elif num <= score[15] and num >= score[29]: print("B+")
elif num <= score[30] and num >= score[34]: print("B0")
elif num <= score[35] and num >= score[44]: print("C+")
elif num <= score[45] and num >= score[47]: print("C0")
else: print("F")