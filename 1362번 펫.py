# https://www.acmicpc.net/problem/1362

# 상태 저장
state = []

# 무한 반복
while 1:
    # 적정체중, 실제체중 입력
    o, w = map(int,input().split())

    # 생존 확인
    death = 0

    # 시나리오 끝
    if o == 0 and w == 0:
        break

    while 1:
        # 수행할 동작 입력
        action, num = input().split()
        num = int(num)
        
        # '# 0'이 입력되면 종료
        if action == '#' and num == 0:
            break

        # 펫이 살아있다면
        if death != 1:
            # 'F'가 입력되면 체중 증가
            if action == 'F':
                w += num
            # 'E'가 입력되면 체중 감소
            elif action == 'E':
                w -= num
                # 펫이 죽었다면
                if w <= 0:
                    death = 1
            
    # 해당하는 상태 저장
    if w > (o/2) and w < (o*2):
        state.append(':-)')
    elif death == 1: # 죽음
        state.append('RIP')
    else: # 슬픔
        state.append(':-(')

# 출력
for i in range(len(state)):
    print(i+1,state[i])