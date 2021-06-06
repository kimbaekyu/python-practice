#2차원 list_2_응용

list1=[]
list2=[]
value=1

for i in range(1,5):
    for k in range(1,6):
        list1.append(k*i)
    list2.append(list1)
    list1=[]
    

for i in range(0,4):
    for k in range(0,5):
        print("%3d" %list2[i][k],end="")
    print("")
