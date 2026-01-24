#문제: 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
#입력: 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
#둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.
#출력: X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.

import sys
n, x = map(int,sys.stdin.readline().split())

n_list = list(map(int,sys.stdin.readline().split()))
# 리스트에 넣어보고


# for + if 문으로 하자
for i in n_list: # in list()>>자료 갯수만큼 반복
    if i <x:
        print(i,end = " ")


# while로 구현하기 > 반복횟수 i(index_list)을 지정해야함
#i = 0
# i가 리스트의 길이(n)보다 작은 동안 반복!
#while i < n:
    #if n_list[i] < x: # x 보다 value가 작은경우
        #print(n_list[i++],end=" ") #value 출력, 끝문자 기본 \n > " " 으로 바꿔서 줄바뀜을 공백으로 수정
    #i +=1