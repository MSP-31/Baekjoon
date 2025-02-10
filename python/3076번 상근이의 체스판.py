# https://www.acmicpc.net/problem/3076

R, A = map(int,input().split())
C, B = map(int,input().split())

for r in range(R):
    for c in range(C):
        for a in range(A):
            for b in range(B):
                # 현재 셀의 행이 짝수일때
                if (r+a) % 2 == 0:
                    print("X",end="")
                # 현재 셀의 행이 홀수일때
                else:
                    print(".",end="")
        print()