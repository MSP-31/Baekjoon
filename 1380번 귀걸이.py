# https://www.acmicpc.net/problem/1380

result = []

while 1:
    num = int(input())
    # '0'이 입력되면 종료
    if num == 0:
        break

    name = []
    temp = []

    # 학생숫자 입력받음
    for i in range(num):
        name.append(input())

    for i in range((num*2)-1):
        count,label = input().split()
        count = int(count)

        # temp의 값이 name에 존재한다면
        if name[count-1] in temp:
            # 삭제
            temp.remove(name[count-1])
        else:
            # 추가
            temp.append(name[count-1])

    # 결과 집어넣음
    result.append(temp.pop())

    temp.clear()
    name.clear()

# 끝
for i in range(len(result)):
    print(i+1,result[i])