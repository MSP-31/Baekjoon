# https://www.acmicpc.net/problem/1316

count = 0

num = int(input())

for i in range(num):
    text = list(input())
    set_text = set(text)

    for j in range(len(text)):
        # set에 해당 값이 존재한다면
        if text[j] in set_text:
            # 현재값과 다음값을 비교해서 같지 않다면
            if j < len(text)-1 and text[j] != text[j+1]:
                # 이어지지 않으므로 set에서 제거
                set_text.remove(text[j])
        # 포함되어있지 않으면 count+1 하고 멈춤
        else:
            count += 1
            break

# 그룹 단어가 아닌경우 - 총 단어 개수
print(num-count)
