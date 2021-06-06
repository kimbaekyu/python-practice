#input gugudan

a=int(input("input num: "))
print("<%d 단>"%(a))
for i in range(1,10,1):
    print("%d X %d = %2d"%(a,i,a*i))
