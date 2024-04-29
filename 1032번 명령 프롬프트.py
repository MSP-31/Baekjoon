# https://www.acmicpc.net/problem/1032

result = []

# 입력받은 만큼 배열 생성
num = [0] * int(input())

for i in range(len(num)):
    num[i] = input()

# 문자열 반복
for i in range(len(num[0])):
    # 각 문자열에서 i번째 문자만 분리함
    char_i = [string[i] for string in num if i < len(string)]
    
    # 모두 같은지 비교
    if all(char == char_i[0] for char in char_i):
        result.append(char_i[0])
    else: # 같지않으면 ? 추가
        result.append("?")

# 리스트를 문자열로 변경
result = "".join(result)
print(result)