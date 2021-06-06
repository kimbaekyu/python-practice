##Variable
select,result,numStr,num1,num2=0,0,"",0,0

##main
while(1):
    
    select=(input("1.수식계산기 2.두 수 사이 합계 3.종료(종료하려면 exit를 입력하세요): "))

    if select=="1":
        numStr=input("*** 수식을 입력하세요 : ")
        result=eval(numStr)
        print("%s 결과는 %5.1f 입니다. "%(numStr,result))

    elif select=="2":
        num1=int(input("***첫번째 수를 입력하세요 : "))
        num2=int(input("***두번째 수를 입력하세요 : "))

        for i in range(num1,num2+1) :
            result=result+i

        print("%d+...+%d = %d"%(num1,num2,result))
    else:
        print("종료합니다.")
        break
