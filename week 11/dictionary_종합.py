#dictionary 활용
## 변수 선언
foods={"떡볶이":"오뎅",
       "짜장면":"단무지",
       "라면":"김치",
       "피자":"피클",
       "맥주":"땅콩",
       "치킨":"치킨무",
       "삼겹살":"상추"}

##메인코드
while(1):
    myfood=input(str(list(foods.keys()))+"중 좋아하는 것은?")
    if myfood in foods:
        print("<%s>궁합 음식은 <%s> 입니다."%(myfood, foods.get(myfood)))

    elif myfood=="끝":
        break
    else:
        print("그런 음식이 없습니다. 다시 확인해 보세요.")
