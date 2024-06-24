# https://www.acmicpc.net/problem/27964
# 서로 다른 4종류의 치즈가 들어가면 yummy 아니면 sad

n = int(input())
toppings = set(input().split())

count = 0
if len(toppings) >= 4:
    for topping in toppings:
        if len(topping) >= 6 and topping[-6:] == 'Cheese':
            count += 1
    

if count >= 4:
    print('yummy')
else:
    print('sad')