# https://www.acmicpc.net/problem/1672

# 리스트로 데이터 테이블 생성
data =  [["A", "C", "A", "G"],
         ["C", "G", "T", "A"],
         ["A", "T", "C", "G"],
         ["G", "A", "G", "T"],]

# 문자를 숫자로 매핑하는 딕셔너리
mapping = {'A':0, 'G':1, 'C':2, 'T':3}

num = int(input())
x = list(input())

# 문자 개수만큼 반복
for i in range(len(x)):
    # 리스트가 비어있지 않은지 확인 (index error 방지)
    if len(x) > 1:
        # 리스트의 마지막 값을 반환하고 제거
        An = x.pop()
        An_1 = x.pop()

        # 문자를 해당하는 숫자로 치환
        An = mapping[An]
        An_1 = mapping[An_1]

        # 치환한 값을 리스트 끝에 추가
        x.append(data[An][An_1])

    # 값이 하나 남았다면
    if len(x) == 1:
        break

print(x[0])