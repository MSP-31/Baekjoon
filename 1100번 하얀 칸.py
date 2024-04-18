# https://www.acmicpc.net/problem/1100

# 홀수일때 1
row_odd = 0
col_odd = 0

# 카운터
count = 0

for i in range(8):
    # 한줄씩 입력받음
    board = input()
    # 행 계산
    row_odd = i % 2
    
    # 입력받은 값 만큼 반복
    for j in range(len(board)):
        # 열 계산
        col_odd = j % 2

        # 홀수 행 일때
        if row_odd:
            # 홀수 열이고 입력받은 값이 F일때
            if col_odd and board[j] == 'F':
                count += 1
        else:
            if not col_odd and board[j] == 'F':
                count += 1
print(count)