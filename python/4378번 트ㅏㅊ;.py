# https://www.acmicpc.net/problem/4378

"""
# 무식하게 딕셔너리로 때려박기
keyboard = {'1':'`','2':'1','3':'2','4':'3','5':'4','6':'5','7':'6','8':'7','9':'8','0':'9','-':'0','=':'-',
           'W':'Q','E':'W','R':'E','T':'R','Y':'T','U':'Y','I':'U','O':'I','P':'O','[':'P',']':'[','\\':']',
           'S':'A','D':'S','F':'D','G':'F','H':'G','J':'H','K':'J','L':'K',';':'L','\'':';',
           'X':'Z','C':'X','V':'C','B':'V','N':'B','M':'N',',':'M','.':',','/':'.'}

while True:
    try:
        text = input()
        result = []
        for i in text:
            if i != ' ':
                result.append(keyboard[i])
            else:
                result.append(i)

        print(''.join(result))

    except EOFError:
        break
"""
while True:
    try:
        text = input()
        # 변환 테이블
        table = text.maketrans('1234567890-=WERTYUIOP[]\\SDFGHJKL;\'XCVBNM,./',
                               '`1234567890-QWERTYUIOP[]ASDFGHJKL;ZXCVBNM,.')
        # 문자 매핑
        result = text.translate(table)
        print(result)
    except EOFError:
        break