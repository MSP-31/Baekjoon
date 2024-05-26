# https://www.acmicpc.net/problem/10988

text = input()

if text == text[::-1]:
    print(1)
else:
    print(0)