##매개변수 전달방법 6_로또복권번호
import random

##함수 정의 부분
def getNumber():
    return random.randrange(1,46)
        

##변수 선언
lotto=[]
num=0

##메인코드
print("##로또 추첨을 시작합니다.##\n")

while True:
    num=getNumber()

    if lotto.count(num)==0: #리스트에서 찾을 값(0)의 개수를 센다.-> 0이 없으면 실행
        lotto.append(num) #리스트 삽입연산 

    if len(lotto)>=6: #로또갯수 6개로 제한
        break

print("추첨된 로또 번호 ==> ",end='')
lotto.sort()
for i in range(0,6):
    print("%d "%lotto[i],end='')
