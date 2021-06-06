# break문을 활용한 프로그램 종료

a,b=0,0
sum=0

while 1:
    a=int(input("Input A : "))
    if a==0:
        print("0을 입력해서 종료합니다.")
        break
    b=int(input("Input B : "))
    sum=a+b
    print("%d + %d = %d"%(a,b,sum))


print("0을 입력해서 반복문을 탈출했습니다.") 
