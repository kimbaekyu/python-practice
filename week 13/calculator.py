##calculator 함수
def calculator(x1,x2,ch):
    hap=0

    if ch=='+':
        hap=x1+x2
        print("%d + %d = %d"%(x1,x2,hap))
    elif ch=='-':
        hap=x1-x2
        print("%d - %d = %d"%(x1,x2,hap))
    elif ch=='/':
        hap=x1/x2
        print("%d / %d = %d"%(x1,x2,hap))
    elif ch=='*':
        hap=x1*x2
        print("%d * %d = %d"%(x1,x2,hap))
    else:
        print("ERROR")

## 변수
a=0
b=0

##메인함수
a=int(input("X1 을 입력해주세요: "))
b=int(input("X2 을 입력해주세요: "))
str=(input("원하는 사칙연산(+,-,/,*)을 입력해주세요: "))
calculator(a,b,str)
