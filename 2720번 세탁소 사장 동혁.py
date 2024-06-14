# https://www.acmicpc.net/problem/2720

def case(change):
    arr = [0] * 4

    if change // 25:
        arr[0] = change // 25
        change %= 25
    
    if change // 10:
        arr[1] = change // 10
        change %= 10
    
    if change // 5:
        arr[2] = change // 5
        change %= 5
    
    if change // 1:
        arr[3] = change // 1
        change %= 1
    
    str_arr = [str(num) for num in arr] # 문자로 변환
    result = ' '.join(str_arr) # 형식 변환

    return result

n = int(input())
result = []

for i in range(n):
    change = int(input())
    result.append(case(change))

for i in range(n):
    print(result[i])
