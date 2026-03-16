#boj 1026 , 곱의 합 최소화


#Pesudo
#1: 곱의 합을 최소화 하려면 어떻게 짝을 지어야 할까요? 예시: B(max) * A(선택) + B(min) * A(선택)
#2: 오름차순정렬 A 내림차순 정렬 B를 한 뒤에 곱하면 된다. 
#3: 단, B의수는 재배열 하면 안된다? > 곱한뒤 다시 원래의 인덱스로 복귀.
#4 S의 최솟값 출력 = A를 출력할 필요는 없네? 곱만 출력.

n = int(input())
a = list(map(int,input().split())) # map(f) iterator 반환하기에, list로 만들어줘야함.
b = list(map(int,input().split()))
result = 0

#a.sort는 제자리정렬이라 none을 반환함. > 변수로 저장할 수 없음! 
#변수로 저장하고 싶다면 sorted(a)사용, 인자는 reverse=True 
a2 = sorted(a, reverse = True) # 내림차순 정렬 sorted(list, reverse = True or False) 생략시 오름차순
b2 = sorted(b) #오름차순 정렬

for i in range(len(a2)):
    result += a2[i] * b2[i] #max(a) * min(b)
print(result)