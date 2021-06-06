## 변수 선언
a,b,sum=0,0,0
end=""
## main 함수

while True :
    if(end=="exit"):
        print("Program Exit")
        break
    else :
        a=int(input("First num: "))
        b=int(input("Second num: "))
        
        sum=a+b
        print("%d + %d = %d"%(a,b,sum))
    print("==========================================")
    end=input("계속하려면 no, 종료하고싶으면 exit를 입력하세요 : ")
    
    
