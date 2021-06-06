 #1부터 원하는숫자 까지의 합
sum=0
a=int(input("Input Num: "))
for i in range(1,a+1,1):
    sum=sum+i

print("1부터 %d 까지 숫자의 합 : %d"%(a,sum))
