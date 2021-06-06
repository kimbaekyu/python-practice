# continue ex1

##변수 선언
sum,i=0,0

## main code

for i in range(1,101):
    if i%3==0:
        continue
    sum+=i

print("1~100의 합계(3의 배수 제외):%d"%sum)
    
