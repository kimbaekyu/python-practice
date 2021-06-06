#shift bit
a=10;b=10;

print("<<SHIFT LEFT START>>")
print("\n")
for i in range(1,5):
    a=a<<i
    print("SHIFT LEFT" ,i ,"=>", a)
    print("===================")
    a=10
print("SHIFT LEFT END")
print("\n")
print("--------------------------------------")
print("\n")
print("<<SHIFT RIGHT START>>")
print("\n")
for i in range(1,5):
    b=b>>i
    print("SHIFT RIGHT ",i,"=>",b)
    print("===================")
    b=10
print("SHIFT RIGHT END")
