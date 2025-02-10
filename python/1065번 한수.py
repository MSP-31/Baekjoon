# https://www.acmicpc.net/problem/1065

n = int(input())

count = 0
# 1부터 n+1 까지 반복
for i in range(1,n+1):
    n_str = str(i)      # i를 문자로
    n_size = len(n_str) # 해당 문자의 길이

    # 길이가 2 이하면 모두 등차수열
    if n_size <= 2:
        count += 1
        continue
    
    # 임시로 값을 저장해둘 배열 생성
    temp = [0] * (n_size - 1)
    for j in range(n_size):
        # n_size의 마지막값 이전이면
        if j != n_size - 1:
            # 해당하는 자릿수와 다음 자릿수를 빼고 임시배열에 저장
            temp[j] = int(n_str[j]) - int(n_str[j+1])
        # 마지막 값이라면
        else:
            # 임시배열안의 모든 값이 동일한지 비교하고 참이면 +1
            if all(element == temp[0] for element in temp):
                count += 1

print(count)