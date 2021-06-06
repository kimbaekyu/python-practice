#윤년계산
year=0
year=int(input("INPUT NUMBER: "))

#윤년결과
if((year%4==0) and (year%100!=0) or (year%400==0)): 
    print("%d 년은 윤년입니다." %year);
else :
    print("%d 년은 윤년이 아닙니다." %year);
