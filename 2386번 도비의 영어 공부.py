# https://www.acmicpc.net/problem/2386

count = []
text = []

while(1):
    # 리스트로 통째로 입력받음
    t = list(input())
    # 그중 첫번째 단어만 소문자로 추출함
    x = t[0].lower()
    # 입력값이 '#' 이라면 멈춤
    if x == '#':
        break
    else:
        # 첫번째 단어와 같은 값만 추출
        result = list(filter(lambda y: y.lower() == x,t))
        num = len(result)
        count.append(len(result)-1)
        text.append(x)

for i in range(len(count)):
    print(text[i],count[i])