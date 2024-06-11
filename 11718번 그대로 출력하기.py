# https://www.acmicpc.net/problem/11718
# EOF를 사용하는 문제
text_list = []

while 1:
    try:
        text = input()
        text_list.append(text)
    except EOFError:
        break

for i in range(len(text_list)):
    print(text_list[i])