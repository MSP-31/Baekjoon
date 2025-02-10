# https://www.acmicpc.net/problem/2941

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count = 0
i = 0

alpha = list(input())

while i < len(alpha):
    # 다음 글자가 있다면
    if i+1 < len(alpha):
        temp = alpha[i] + alpha[i+1]
        # 합친 글자가 크로아티아 알파벳이라면
        if temp in croatia:
            count += 1
            i += 2
            continue
        # 2글자 더 있다면
        if i+2 < len(alpha):
            # temp에 하나더 추가
            temp += alpha[i+2]
            if temp in croatia:
                count += 1
                i += 3
                continue
    
    count += 1
    i += 1

print(count)