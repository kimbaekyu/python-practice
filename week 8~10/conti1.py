#1~100까지의 합을 구하되 3의 배수를 건너뛰고 더하는 프로그램
hap=0

for i in range(1,101):
    if i%3==0:
        continue
    hap+=i

print("1~100까지의 합 %d"%hap)    
