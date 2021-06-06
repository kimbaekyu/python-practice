## 변수 선언
a,b,sum=0,0,0
ch,end="",""
## main 함수

while True :
    
    a=int(input("First num: "))
    b=int(input("Second num: "))
    ch=input("연산자를 입력해주세요: ")
    
    if(end=="exit"):
        print("Program Exit")
        break

    elif ch=="+":
        sum=a+b
        print("%d + %d = %d"%(a,b,sum))

    elif ch=="-" :
        sum=a-b
        print("%d - %d = %d"%(a,b,sum))

    elif ch=="*" :
        sum=a*b
        print("%d * %d = %d"%(a,b,sum))
    

    elif ch=="//" :
        sum=a//b
        print("%d // %d = %d"%(a,b,sum))

    elif ch=="/" :
        sum=a/b
        print("%d / %d = %lf"%(a,b,sum))

    elif ch=="**" : 
        sum=a**b
        print("%d ** %d = %d"%(a,b,sum))

    else :
        print("연산자를 다시 입력하세요")

    end=input("계속하려면 yes, 종료하고싶으면 exit를 입력하세요 : ")
    print("==========================================")    
