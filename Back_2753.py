# 윤년이면 1, 아니면 0을 출력하는 문제

year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('1')
else : 
    print('0')