# https://www.acmicpc.net/problem/7789
import math

# 소수 체크 함수
def is_prime_number(x):
    # x의 제곱근까지 소수 체크함, 그 이상은 결과가 같기때문
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 만약 2이상의 수에서 나누어 떨어지면
        if x % i == 0:
            # 소수가 아니므로 false
            return False
    return True

n, s = input().split()

s = int(s+n)
n = int(n)

if is_prime_number(n):
    if is_prime_number(s):
        print("Yes")
    else:
        print("No")
else:
    print("No")
