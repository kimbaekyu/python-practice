##매개변수 전달방법 3

##함수 정의 부분
def para_func(x1,x2=0,x3=0,x4=0,x5=0,x6=0,x7=0,x8=0,x9=0,x10=0):
    result=0
    result=x1+x2+x3+x4+x5+x6+x7+x8+x9+x10
    return result
##변수 선언
hap=0
a=[0,0,0,0,0,0,0,0,0,0]
num=0

##메인코드
num=int(input("더하고 싶은 숫자의 갯수(1~10): "))
if num==1:
    a[0]=int(input("input x1: "))
    hap=para_func(a[0])
    print("매개변수 %d개 함수 호출 결과====>%d"%(num,hap))

elif num==2:
    for i in range(1,3):
        a[i-1]=int(input("input x%d: "%(i)))
    hap=para_func(a[0],a[1])
    print("매개변수 %d개 함수 호출 결과====>%d"%(num,hap))

elif num==3:
    for i in range(1,4):
        a[i-1]=int(input("input x%d: "%(i)))
    hap=para_func(a[0],a[1],a[2])
    print("매개변수 %d개 함수 호출 결과====>%d"%(num,hap))

elif num==4:
    for i in range(1,5):
        a[i-1]=int(input("input x%d: "%(i)))
    hap=para_func(a[0],a[1],a[2],a[3])
    print("매개변수 %d개 함수 호출 결과====>%d"%(num,hap))

elif num==5:
    for i in range(1,6):
        a[i-1]=int(input("input x%d: "%(i)))
    hap=para_func(a[0],a[1],a[2],a[3],a[4])
    print("매개변수 %d개 함수 호출 결과====>%d"%(num,hap))

elif num==6:
    for i in range(1,7):
        a[i-1]=int(input("input x%d: "%(i)))
    hap=para_func(a[0],a[1],a[2],a[3],a[4],a[5])
    print("매개변수 %d개 함수 호출 결과====>%d"%(num,hap))

elif num==7:
    for i in range(1,8):
        a[i-1]=int(input("input x%d: "%(i)))
    hap=para_func(a[0],a[1],a[2],a[3],a[4],a[5],a[6])
    print("매개변수 %d개 함수 호출 결과====>%d"%(num,hap))

elif num==8:
    for i in range(1,9):
        a[i-1]=int(input("input x%d: "%(i)))
    hap=para_func(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7])
    print("매개변수 %d개 함수 호출 결과====>%d"%(num,hap))

elif num==9:
    for i in range(1,10):
        a[i-1]=int(input("input x%d: "%(i)))
    hap=para_func(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8])
    print("매개변수 %d개 함수 호출 결과====>%d"%(num,hap))

elif num==10:
    for i in range(1,11):
        a[i-1]=int(input("input x%d: "%(i)))
    hap=para_func(a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9])
    print("매개변수 %d개 함수 호출 결과====>%d"%(num,hap))

else:
    print("ERROR\n허용된 범위를 벗어났습니다.")

