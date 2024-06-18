# https://www.acmicpc.net/problem/4949

result = []
while True:
    text = input()
    
    if text == ".":
        break
    theses = []
    balanced = True

    for i in range(len(text)):
        t = text[i]
        if t in "([":
            theses.append(t)
        elif t in ")]":
            if not theses or (t == ")" and theses[-1] != "(") or (t == "]" and theses[-1] != "["):
                balanced = False
                break
            theses.pop()
    
    # 스택이 비었는지 확인
    if balanced and not theses:
        result.append("yes")
    else:
        result.append("no")

for i in result:
    print(i)