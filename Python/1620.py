#1620



#pesudo
#1. N, M 입력
#2. N번 반복: 이름 입력 → 두 딕셔너리에 저장
#3. M번 반복: try: get으로 value 추출, except: keys로 key 추출

#4. sys.stdin.readline 사용 (속도)

import sys

input = lambda: sys.stdin.readline().rstrip('\n')

n, m = map(int,input().split())

poke_dic_1 = {}
poke_dic_2 = {}

for i in range(n): #name to num dic name:num
    name = input()
    poke_dic_1[name] = i +1 #0-base key= name , number = value

    poke_dic_2[i+1] = name # 0 base, key = number, value = name

for i in range(m):
    question = input()
    try:
        num = int(question) # if question is number > print value
        print(poke_dic_2[num]) # num > name
    except:
        print(poke_dic_1[question]) #name > num

        

