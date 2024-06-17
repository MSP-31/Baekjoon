# https://www.acmicpc.net/problem/2309

def function():
    for i in range(9):
        x = stature[i]
        for j in range(i+1,9):
            y = stature[j]

            sum = x + y
            if 100 == (total_stature - sum):
                stature.remove(x)
                stature.remove(y)
                stature.sort()
                return

stature = [0] * 9

for i in range(9):
    stature[i] = int(input())
total_stature = sum(stature)

function()

for i in stature:
    print(i)