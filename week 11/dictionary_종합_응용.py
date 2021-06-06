#dictionary 활용_응용
## 변수 선언
animals={"소":"송아지",
         "말":"망아지",
         "개":"강아지",
         "닭":"병아리"
         }
##메인코드

while(1):
    babyAnimal=input(str(list(animals.keys()))+"중 궁금한 새끼동물의 이름은?")
    
    if babyAnimal in animals :
        print("%s의 새끼동물 이름은 %s입니다"%(babyAnimal,animals.get(babyAnimal)))
                     
    elif babyAnimal=="끝":
        break
    else:
        print("찾을 수 없습니다. 다시 입력해 주세요.")
