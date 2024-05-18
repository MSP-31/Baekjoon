# https://www.acmicpc.net/problem/1181

n = int(input())
word = {}

for i in range(n):
    text = input()
    word[text] = len(text)

# 문자 길이, 사전순으로 정렬
sorted_word = sorted(word.keys(), key=lambda x: (word[x], x))

for i in sorted_word:
    print(i)