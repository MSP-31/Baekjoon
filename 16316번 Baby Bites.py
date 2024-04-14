"""
문제
Arild just turned 1 year old, and is currently learning how to count. His favorite thing to count is how many mouthfuls he has in a meal: every time he gets a bite, he will count it by saying the number out loud.

Unfortunately, talking while having a mouthful sometimes causes Arild to mumble incomprehensibly, making it hard to know how far he has counted. Sometimes you even suspect he loses his count! You decide to write a program to determine whether Arild’s counting makes sense or not.

입력
The first line of input contains an integer n (1 ≤ n ≤ 1 000), the number of bites Arild receives. Then second line contains n space-separated words spoken by Arild, the i’th of which is either a non-negative integer ai (0 ≤ ai ≤ 10 000) or the string “mumble”.

출력
If Arild’s counting might make sense, print the string “makes sense”. Otherwise, print the string “something is fishy”.

예제 입력 1 
5
1 2 3 mumble 5
예제 출력 1 
makes sense

예제 입력 2 
8
1 2 3 mumble mumble 7 mumble 8
예제 출력 2 
something is fishy

예제 입력 3 
3
mumble mumble mumble
예제 출력 3 
makes sense
"""
count = int(input())
num = list(input().split())

# 이상 체크
check = True

for i in range(count):
    # 숫자인지 판별
    if num[i].isdigit():
        # 숫자라면 순서가 같은지 확인
        if int(num[i]) != i+1:
            check = False
            break
    # 문자일때 mumble이라면 통과
    elif num[i] == 'mumble':
        continue
    
    # 해당하지 않으면
    else:
        check = False
        break

if check:
    print('makes sense')
else:
    print('something is fishy')