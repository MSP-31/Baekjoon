# https://www.acmicpc.net/problem/12760

n,m = map(int,input().split())

nums = []
score = [0] * n

# 인원수 만큼 입력받음
for i in range(n):
    num = list(map(int,input().split()))

    # 내림차순 정렬
    num.sort(reverse=True)
    nums.append(num)

# 카드 개수만큼 반복
for i in range(m):
    # 해당 열의 최대값
    nx = max(x[i] for x in nums)

    # 값 비교
    for j in range(n):
        # 같은 값이면 +1점
        if nx == nums[j][i]:
            score[j] += 1

# 최고 점수 저장
nx = max(score)
for i in range(n):
    # 최고점수와 같다면 출력
    if nx == score[i]:
        print(i+1,end=" ")