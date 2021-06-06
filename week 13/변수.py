## 변수 선언
a=20

##함수 정의
def func1():
    a=10
    print("func1의 a: %d"%a)
    a=40
    print("func1의 a: %d"%a)

def func2():
    print("func2의 a: %d"%a)

##main
func1()
func2()

