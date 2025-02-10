"""
문제
영문 문장을 입력받아 모음의 개수를 세는 프로그램을 작성하시오. 모음은 'a', 'e', 'i', 'o', 'u'이며 대문자 또는 소문자이다.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있으며, 각 줄마다 영어 대소문자, ',', '.', '!', '?', 공백으로 이루어진 문장이 주어진다. 각 줄은 최대 255글자로 이루어져 있다.

입력의 끝에는 한 줄에 '#' 한 글자만이 주어진다.

출력
각 줄마다 모음의 개수를 세서 출력한다.

예제 입력 1 
How are you today?
Quite well, thank you, how about yourself?
I live at number twenty four.
#
예제 출력 1 
7
14
9
"""
# 모음 개수 저장용 빈 배열 생성
num = []
# 찾고자 하는 모든 모음 리스트
search_char = ['a', 'e', 'i', 'o', 'u']

while True:
    text = input()

    # '#'이 입력되면 브레이크
    if text.lower() == '#':
        break

    else:
        # 입력받은 텍스트를 리스트로 만듬
        text_list = list(text.lower())
        # 리스트 컴프리헨션을 이용하여 찾는 문자만 남기고 모두 제거한 리스트를 저장 
        filter_list = [char for char in text_list if char in search_char]
        # 문자열에서 해당되는 문자들의 숫자만 세서 배열에 저장
        num.append(len(filter_list))

for i in range(len(num)):
    print(num[i])