##매개변수 전달방법 1

##함수 정의 부분
def para2_func(x1,x2):
    result=0
    result=x1+x2
    return result

def para3_func(x1,x2,x3):
    result=0
    result=x1+x2+x3
    return result

##변수 선언
hap=0
a,b,c=0,0,0

##메인코드
a=int(input("input x1: "))
b=int(input("input x2: "))
hap=para2_func(a,b)
print("매개변수 2개 함수 호출 결과====>%d"%hap)

a=int(input("input x1:"))
b=int(input("input x2:"))
c=int(input("input x3:"))
hap=para3_func(a,b,c)
print("매개변수 3개 함수 호출 결과====>%d"%hap)
