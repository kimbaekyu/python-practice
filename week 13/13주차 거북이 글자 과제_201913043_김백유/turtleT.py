import turtle
import random
from tkinter.simpledialog import *

## 전역 변수 선언
swidth,sheight=300,300
tSize=0;
inStr=""
## 메인 코드

turtle.title('거북이 글자쓰기')
turtle.shape('turtle')
turtle.setup(width=swidth+50, height=sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup()
while(True):
    inStr = askstring('문자열 입력', "거북이 쓸 문자열을 입력")

    for ch in inStr :
    
        tX = random.randrange(-swidth / 2, swidth / 2)

        tY = random.randrange(-sheight / 2, sheight / 2)

        r = random.random()
        g = random.random()
        b = random.random()

        tSize = random.randrange(10, 70)

        turtle.goto(tX,tY)
        turtle.pencolor((r, g, b))
        turtle.write(ch, font=('맑은 고딕', tSize, 'bold'))

turtle.done()
