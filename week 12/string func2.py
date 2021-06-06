# 문자열 함수 활용2
before=['2021','05','21']
print("before : ",before)
after=list(map(int,before))
print("after : ",after)

str1="파이썬   Python   Java     자바"
str2=""

for i in range(0,len(str1)):
    if str1[i]!=' ':
        str2+=str1[i]

print("원래 문자열==>"+'['+str1+']')
print("공백제거  문자열==>"+'['+str2+']')

str3=input("입력문자열==> ")
print("출력 문자열===>",end='')
for i in range(0,len(str3)):
    if str3[i]=='o':
        print('#',end='')
    else:
        print(str3[i],end='')

print("")

print("replace() 이용:",str3.replace('o','$'))
