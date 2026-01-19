
a,b = map(int,input('숫자두번').split())


if b >= 45: # 시간이 변하지 않는 경우
    b -= 45
elif b < 45 and a!= 0:
    a -= 1
    b = 60 + (b -45)
else: # 45분 이하면서 a ==0 시 인경우
    a = 23
    b = 60 + (b -45)
print(a,b)

