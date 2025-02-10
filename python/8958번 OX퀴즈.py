# https://www.acmicpc.net/problem/8958

counts = []
num = int(input())

for i in range(num):
    count = 0  # 총 개수
    degree = 0 # 차수
    text = list(input())
    
    for x in text:
        if x == 'O':
            degree += 1
            count += degree
        else: # 차수 초기화
            degree = 0
    
    counts.append(count)

for i in range(len(counts)):
    print(counts[i])