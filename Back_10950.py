# 두 정수 A와 B를 입력받은 다음, A + B를 출력하는 프로그램을 작성하십시오.

case = int(input())

for i in range(case):
    a, b = map(int, input().split())
    print(a + b)