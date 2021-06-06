##calculator module
def cal():
    result=0.0
    x1=float(input("INPUT X1: "))
    ch=input("연산자(+,-,*,/,**,//,%)를 입력하세요: ")
    x2=float(input("INPUT X2: "))
    
    print("**모듈로 작성한 계산기 호출 결과***")
    
    if ch=='+':
        result=x1+x2
        print("%.3f + %.3f = %.3f"%(x1,x2,result))
    elif ch=='-':
        result=x1-x2
        print("%.3f - %.3f = %.3f"%(x1,x2,result))
    elif ch=='*':
        result=x1*x2
        print("%.3f * %.3f = %.3f"%(x1,x2,result))
    elif ch=='/':
        result=x1/x2
        print("%.3f / %.3f = %.3f"%(x1,x2,result))
    elif ch=='**':
        result=x1**x2
        print("%.3f ** %.3f = %.3f"%(x1,x2,result))
    elif ch=='//':
        result=x1//x2
        print("%.3f // %.3f = %.3f"%(x1,x2,result))
    elif ch=='%':
       result=x1 % x2
       print("%.3f %% %.3f = %.3f"%(x1,x2,result))
    else:
        print("연산기호를 잘못 입력하였습니다.")

    print("")
