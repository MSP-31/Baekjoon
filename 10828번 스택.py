# https://www.acmicpc.net/problem/10828
# 시간 제한때문에 빠른 입출력 사용
import sys

stack = []

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    cmd = sys.stdin.readline().rstrip().split()

    if cmd[0] == 'push':
        stack.append(cmd[1])

    elif cmd[0] == 'pop':
        try:
            print(stack.pop())
        except IndexError:
            print(-1)

    elif cmd[0] == 'size':
        print(len(stack))

    elif cmd[0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
    
    elif cmd[0] == 'top':
        try:
            print(stack[-1])
        except IndexError:
            print(-1)
        