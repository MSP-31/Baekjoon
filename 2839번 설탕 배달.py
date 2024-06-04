# https://www.acmicpc.net/problem/2839

n = int(input())

count = 0

# 5로 최대한 나눔
count += n // 5
n %= 5

# 남은 값이 있다면
while n > 0:
    # 3으로 눠진다면
    if (n % 3) == 0:
        # 나눈값을 모두 더하고 끝
        count += n // 3
        n %= 3
        break
    # 나눠지지 않는다면
    else:
        # count가 남아있으면
        if count > 0:
            # count를 제거하고 다시 5를 추가
            count -= 1
            n += 5
        # count가 없다면 멈춤
        else:
            break

# 만약에 다 나눠지지 않았다면
if n != 0:
    count = -1

print(count)
