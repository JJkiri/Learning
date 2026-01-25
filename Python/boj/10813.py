#문제: 도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다. 바구니에는 공이 1개씩 들어있고,
# 처음에는 바구니에 적혀있는 번호와 같은 번호가 적힌 공이 들어있다.도현이는 앞으로 M번 공을 바꾸려고 한다.
# 도현이는 공을 바꿀 바구니 2개를 선택하고, 두 바구니에 들어있는 공을 서로 교환한다.
# 공을 어떻게 바꿀지가 주어졌을 때, M번 공을 바꾼 이후에 각 바구니에 어떤 공이 들어있는지 구하는 프로그램을 작성하시오.

#입력: 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
# 둘째 줄부터 M개의 줄에 걸쳐서 공을 교환할 방법이 주어진다. 각 방법은 두 정수 i j로 이루어져 있으며,
# i번 바구니와 j번 바구니에 들어있는 공을 교환한다는 뜻이다. (1 ≤ i ≤ j ≤ N)
# 도현이는 입력으로 주어진 순서대로 공을 교환한다.

#출력: 1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다.

#input , (1)index length = n 을 제공함 (2) range = m 을 제공

import sys

n, m = map(int,sys.stdin.readline().split())

# 바구니와 적혀있는 번호가 같은 번호가 적힌 공 생성
basket = list(range(1,n+1)) # value값 > value num 맞추기 위해 +1 추가

#exchange
#> temp1 , temp2
temp1 = []
temp2 = []
for x in range(0,m):
    i, j = map(int,sys.stdin.readline().split())
    #temp1 = basket[i-1] # 임시저장
    #temp2 = basket[j-1] # 입력값 > index num으로 돌아가기위해 입력값 i,j 에 -1 추가

    #basket[i-1] = temp2 # 교환완료
    #basket[j-1] = temp1 # temp를 굳이 갈 필요 없이 교환단위를 바꿔주면 됨

    basket[i-1], basket[j-1] = basket[j-1], basket[i-1] #index num 으로 찾아가므로 -1 로 입력값과 차이 조정
#output

for x in basket:
    print(x, end = " ")

#print(*basket) < 정답과 동일한 출력, 리스트의 구분자를 공백으로 print
#print(basket, end = " ") <<마지막 줄바뀜 대신 공백 추가