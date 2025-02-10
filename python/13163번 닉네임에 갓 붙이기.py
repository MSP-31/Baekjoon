num = int(input())
name = [0] * num

for i in range(num):
    temp = input()
    # 첫번째 공백을 찾음
    first_space = temp.find(' ')
    
    # 공백이 있을때
    if first_space != -1:
        # 첫번째 공백 이후의 문자만 공백을 제거해서 저장
        temp = temp[first_space+1:].replace(' ','')
        # 남은 문자에 god를 붙여서 저장
        name[i] = 'god' + temp

for i in range(num):
    print(name[i])