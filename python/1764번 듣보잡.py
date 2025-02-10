# https://www.acmicpc.net/problem/1764

n,m = map(int,input().split())

listen = set()
see = set()

# 듣도 못한 사람의 수
for i in range(n):
    listen.add(input())

# 보도 못한 사람의 수
for i in range(m):
    see.add(input())

# 듣도 못한 사람과 보도 못한 사람의 교집합
result = listen.intersection(see)
# 사전순으로 정렬
sort_result = sorted(list(result))


print(len(sort_result))
for result in sort_result:
    print(result)