#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

#10952는 종료시 0 0 if문으로 탈출가능했지만
#10951은 입력이 그냥 끝나므로, while True, try-except 활용해보자
import sys


while True:
# 여기서 try 없이 바로 a, b 대입시 Value Error 발생
    try:
        a, b = map(int,sys.stdin.readline().split())
        print(a+b)
    except: # eof처리 break
        break


# 여기서 제출시 Value Error 발생
# "입력의 개수가 주어지지 않는 경우"는 십중팔구 이 EOF 처리(End of File) >> try except