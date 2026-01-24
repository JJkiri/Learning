# 1 왜 input() 대신 sys.stdin.readline()을 쓰나요
# input(): 입력을 받을 때마다 값을 하나하나 처리하고, 메시지를 띄울 준비도 하며, 입력받은 값의 끝을 확인하는 등 내부적으로 하는 일이 많습니다. (느린 우체국)
# sys.stdin.readline(): 사용자가 입력한 값을 일단 커다란 창고(버퍼)에 몽땅 담아두었다가 한꺼번에 읽어옵니다. 훨씬 단순하고 빠릅니다. (특급 택배)

# 2 어떻게 쓰나요
# import sys # sys라는 도구 상자를 가져옵니다.
# data = sys.stdin.readline()

# 3 .rstrip()은 왜 붙이나요? (개행문자의 비밀)
# 이 부분이 초보자분들이 가장 많이 실수하는 구간입니다. readline()은 이름 그대로 "한 줄을 통째로 읽어오는" 기능입니다.
# 여기서 중요한 점은 사용자가 입력을 마치고 누르는 엔터(Enter) 키까지도 '문자로' 취급해서 가져온다는 것입니다.
# input()은 "Hello"만 가져옵니다.
# sys.stdin.readline()은 "Hello\n"을 가져옵니다.
# 여기서 \n은 '줄바꿈(엔터)'을 의미하는 특수 문자입니다. 이를 개행문자라고 부릅니다.

# 4 .rstrip()을 안쓰면?
# 문자열 비교를 할 때 문제가 생깁니다.
# "Hello"와 "Hello\n"은 컴퓨터 눈에는 완전히 다른 글자이기 때문에, if data == "Hello": 라고 써도 거짓(False)이 나옵니다.

# 5 .rstrip의 역할
# rstrip()은 문자열의 오른쪽(right) 끝에 있는 공백이나 줄바꿈 기호(\n)를 싹둑 잘라내는(strip) 역할을 합니다.

# 6 sys.stdin.readline()은 문자열로 받기때문에, 반드시 변환을 해줘야 합니다.

# 입력:첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.
# 출력: 각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

import sys
T = int(sys.stdin.readline().rstrip())
for i in range(0,T):
    A, B = map(int,sys.stdin.readline().split())
    print(A+B)