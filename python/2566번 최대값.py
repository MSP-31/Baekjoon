# https://www.acmicpc.net/problem/2566

arr = []
falg = False # 반복문 탈출용

for _ in range(9):
    arr.append(list(map(int,input().split())))

# 최대값 출력
arr_max = max(map(max,arr))
print(arr_max)

for i in range(9):
    for j in range(9):
        if arr[i][j] == arr_max:
            print(i+1,j+1)
            falg = True
            break
    if falg:
        break