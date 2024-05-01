# https://www.acmicpc.net/problem/1270
# 보이어-무어 다수결 투표 알고리즘 활용
result = []

num = int(input())

for i in range(num):
    arr = list(map(int,input().split()))
    k = arr.pop(0)

    count = 0 # 과반수의 군대 병사 수
    major = 0 # 과반수의 군대

    for ele in arr:
        # 병사가 0번 등장했다면
        if count == 0:
            # 과반수 군대 교체
            major = ele
        # 현재 과반수 군대의 병사일 경우
        if major == ele:
            count += 1
        else:
            count -= 1

    m = 0 # 과반수 체크용
    for ele in arr:
        if ele == major:
            m += 1

    # 현재 군대가 과반수에 미치지 못하면
    if m > k//2:
        result.append(major)
    else:
        result.append("SYJKGW")

for i in result:
    print(i)