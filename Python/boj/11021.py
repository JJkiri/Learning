    #문제: 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
    #입력: 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
    #출력: 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.

import sys

T = int(input())

for i in range(1,T+1):
    A, B = map(int,sys.stdin.readline().split()) #오류1: int(sys.stdin.readline())은 불가>> sys.stdin.readline은 str "리스트"를 반영하기 때문.
    print(f"Case #{i}: {A+B}") # CASE, Case capital letters 구분 잘할것. 채점오류 발생!