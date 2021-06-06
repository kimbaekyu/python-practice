import turtle
import random

## 전역 변수 선언
myTurtle,tX,tY,tColor,tSize,tShape=0,0,0,0,0,0
shapeList=[]
playerTurtles=[] #거북 2차원 리스트
swidth, sheight=500,500 #큰 사각형 넓이, 높이

## 메인 코드
if __name__=="__main__":
    turtle.title('거북 리스트 활용')
    turtle.setup(width=swidth+50,height=sheight+50)
    turtle.screensize(swidth,sheight)#터틀그래픽 창 넓이, 높이

    shapeList=turtle.getshapes()#다각형 모양
    
    for i in range(0,100):#1차원 리스트를 100개 생성해서 2차원 리스트에 저장
        random.shuffle(shapeList)#무작위로 모양 섞음
        myTurtle=turtle.Turtle(shapeList[0])#현재 거북이
        tX=random.randrange(-swidth/2,swidth/2)#임의의 X 좌표
        tY=random.randrange(-sheight/2,sheight/2)#임의의 y 좌표
        r=random.random()
        g=random.random()
        b=random.random()
        tSize=random.randrange(1,3)#거북이 크기
        playerTurtles.append([myTurtle,tX,tY,tSize,r,g,b])#[현재거북이,임의의 x좌표,임의의 y좌표,거북이 크기,거북이 색상(r),거북이 색상(g),거북이 색상(b)]

    for tList in playerTurtles:#거북이 이동
        myTurtle=tList[0]
        myTurtle.color((tList[4],tList[5],tList[6]))
        myTurtle.pencolor((tList[4],tList[5],tList[6]))
        myTurtle.turtlesize(tList[3])
        myTurtle.goto((tList[1],tList[2]))
    turtle.done()
