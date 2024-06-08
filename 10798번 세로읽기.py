# https://www.acmicpc.net/problem/10798

text = []

for i in range(5):
    text_list = input()
    text.append(text_list)

max_len = max(len(t) for t in text)

# 최대 글자 개수만큼 반복
for i in range(max_len):
    # text의 크기만큼 반복
    for j in range(len(text)):
        # 글자개수가 기준치를 초과하지 않으면
        if i < len(text[j]):
            # j번째 줄의 i번째 글자 출력
            print(text[j][i],end="")