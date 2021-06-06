# break ex1

##변수 선언
sum,i=0,0

## main code

for i in range(1,101):
    sum+=i
    
    if sum>=1000:
        break
    

print("1~100의 합에서 최초로 1000이 넘는 위치 :%d"%i)    
