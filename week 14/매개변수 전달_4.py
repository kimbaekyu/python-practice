##매개변수 전달방법 4_튜플로 전달

##함수 정의 부분
def para_func(*x):
    result=0
    for num in x:
        result=result+num
    return result

##변수 선언
hap=0

##메인코드
hap=para_func(10,20)
print("매개변수 2개 함수 호출 결과===>%d"%hap)
hap=para_func(10,20,40)
print("매개변수 3개 함수 호출 결과===>%d"%hap)
hap=para_func(10,20,30,40,50,60,70,80,90,100)
print("매개변수 10개 함수 호출 결과===>%d"%hap)
