##변수 선언
num=0
ch=65

## 함수 정의 부분
def coffee_machine(button):
    print()
    print("# 1. 뜨거운 물을 준비한다.")
    print("# 2. 종이컵을  준비한다.")
    
    if button==1:
        print("# 3. 보통커피를 탄다.")
    elif button==2:
        print("# 3. 설탕커피를 탄다.")
    elif button==3:
        print("# 3. 블랙커피를 탄다.")
    else:
        print("# 3. 아무 커피나 탄다.")

    print("# 4. 물을 붓는다.")
    print("# 5. 스푼으로 저어서 녹인다.")
    print()
    
    

def client(button,ch):    
    
    if button==1:
        print("%s 손님 보통커피 여기 있습니다."%(chr(ch)))
    elif button==2:
        print("%s 손님 설탕커피 여기 있습니다."%(chr(ch)))
    elif button==3:
        print("%s 손님 블랙커피 여기 있습니다."%(chr(ch)))
    else:
        print("%s 손님 아무커피 여기 있습니다."%(chr(ch)))
    print("----")

    
    
    
## 메인코드
while(True):
    num=int(input("%s 손님 어떤 커피 드릴까요? (1:보통 2:설탕 3:블랙 4.영업종료) "%(chr(ch))))
    if num==4:
        print("영업을 종료합니다.")
        print("=================")
        break
    else:
        coffee_machine(num)
        client(num,ch)
        ch=ch+1
    print("=================")

