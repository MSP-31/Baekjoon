# https://www.acmicpc.net/problem/2851
# 100 이하 수를 고려하지 않아서 틀렸었음

sum = 0
num = []
for i in range(10):
    num.append(int(input()))

for i in range(10):
    sum += num[i]
    if sum >= 100:
        if (sum - 100) > abs((sum - num[i]) - 100):
            print(sum - num[i])
        elif (sum - 100) == abs((sum - num[i]) - 100):
            print(sum)
        else:
            print(sum)
        break
    elif sum < 100 and i == 9:
        print(sum)
