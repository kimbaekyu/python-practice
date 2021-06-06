#input sum
num1,num2,num3,i,sum=0,0,0,0,0
num1=int(input("Start num : "))
num2=int(input("End num : "))
num3=int(input("Increasing Value  : "))

for i in range(num1,num2+1,num3):
    sum=sum+i

print("%d부터 %d까지 %d증가한 값의 합은 : %d"%(num1,num2,num3,sum))
