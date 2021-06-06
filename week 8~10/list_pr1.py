# 리스트 practice_1

num=[0,0,0,0]
sum=0

for i in range(0,4):
    num[i]=int(input("Input Num : "))

for k in range(0,4):
    sum+=num[k]
    print(sum)

print("합계==>%d"%sum)
