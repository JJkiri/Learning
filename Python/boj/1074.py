#1074


#pesudo

#1 4*4를 4등분하면 2*2가 2*2개, 6*6 은 2*2가 3*3개 8*8 은 2*2 가 4*4개
#2 r,c가 어느 작은 사각형에서 사분면인지 알면, 앞의 칸을 건너뛸 수 있다.

n, r, c = map(int,input().split()) #입력받기 n= 2^n행렬 r 행 c 열

def solve(n,r,c): # 2^n행렬에서 r,c가 몇번째 인가? >
    if n == 0: #재귀는 종료조건부터
        return 0 # 2^0 == 1*1행렬. 종료
    
    half = 2**(n-1) #2^n 행렬을 반반 나누는 경계선(십자)
    if r < half and c < half: #왼쪽위, 0
       return solve(n-1,r,c) 

    elif r < half and c >= half: #오른쪽 위, 1
        return half * half + solve(n-1,r, c - half) # half*half 만큼 건너뛰고, c -half 반토막
    
    elif r >= half and c < half: #왼쪽 아래, 2
       return half*half*2 + solve(n-1,r-half,c) # 2칸 건너뛰고, r 반토막
    
    elif r >= half and c >= half: #오른쪽 아래 3
       return half*half*3 + solve(n-1,r-half,c-half)


print(solve(n, r, c))

