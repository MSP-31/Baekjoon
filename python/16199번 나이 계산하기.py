# https://www.acmicpc.net/problem/16199

# 태어난 연도
y, m, d = map(int,input().split())
# 기준날짜
dy, dm, dd = map(int,input().split())

# 연 나이 계산
age_yer = dy - y 

age_man = 0 # 만 나이
# 만나이 계산
if y < dy: # 태어난 연도보다 기준 연도가 더 크면
    if m < dm: # 태어난 달보다 기준 달이 더 클때
        age_man = age_yer

    elif m > dm:
        age_man = age_yer - 1

    else: # 달이 같을 때
        if d <= dd: # 기준 일이 같거나 더 클때
            age_man = age_yer
        else:
            age_man = age_yer - 1
            
# 세는 나이 계산
age_count = age_yer + 1

print(age_man)
print(age_count)
print(age_yer)