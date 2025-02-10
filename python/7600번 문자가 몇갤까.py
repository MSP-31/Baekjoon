# https://www.acmicpc.net/problem/7600

# 개수 저장용 배열
num = []

while True:
    text = input()
    count = 0

    if text == '#':
        break

    else:
        text_list = list(text.lower())
        # a부터 z까지 반복
        for char in range(ord('a'), ord('z')+1):
            temp = False
            # 해당하는 알파벳이 존재하는지 확인
            while chr(char) in text_list:
                # 존재하면 제거
                text_list.remove(chr(char))
                temp = True
            # 해당하는 알파벳이 있다면
            if temp:
                count += 1
        num.append(count)

for i in range(len(num)):
    print(num[i])