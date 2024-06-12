# https://www.acmicpc.net/problem/5622

dials = ['ABC','DEF','GHI','JKL','NMO','PQRS','TUV','WXYZ']
words = input()

sum = 0
for word in words:
    # enumerate 함수는 인덱스와 요소를 반환한다.
    for index,dial in enumerate(dials):
        if word in dial:
            index += 3
            break
    sum += index

print(sum)