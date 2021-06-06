# 문자열 함수 활용4

str1=input("날짜(연/월/일) 입력==>")
print("입력한 날짜의 10년 후는==>",end="")
str2=str1.split('/')


for i in range(0,len(str2)):
    if i==0:
        print(str(int(str2[i])+10)+"년",end='')

    elif i==1:
        print(str2[i]+"월",end='')

    else:
        print(str2[i]+"일")
    
