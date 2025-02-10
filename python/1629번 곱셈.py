# https://www.acmicpc.net/problem/1629
# 만약 (a)와 (b)가 (p)로 나눈 나머지가 서로 동일하다면, (a^k)와 (b^k)을 (p)로 나눈 나머지도 서로 동일하다

def power(a,b):
    result = 1
    while b:
        # b 가 홀수일때
        if b % 2 == 1:
            # reuslt에 a를 한번더 곱함 (+1)
            result *= a
        a *= a   # 제곱
        a = a%c  # 모듈러 연산
        b = b//2 # 분할

    return result

a, b, c = map(int,input().split())

print(power(a,b)%c)