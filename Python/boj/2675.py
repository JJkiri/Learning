#문제: 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
#즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
#QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

import sys
t = int(input())

for i in range(0,t):
    r, word = sys.stdin.readline().split()
    for j in range(0,len(word)):
        P = word[j] * int(r)
        print(P,end="")
    print()
#print()는 기본적으로 \n이 들어가있음
#print(\n)을하는 경우, 두번 줄바꾸게 되어 빈줄이 추가로 생김!