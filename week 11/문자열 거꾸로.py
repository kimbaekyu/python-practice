#문자열 반대로 출력
string1=input("문자열을 입력하세요: ")
string2=""
strlen=len(string1)

for i in range(0,strlen):
    string2+=string1[strlen-(i+1)]

print("내용을 거꾸로 출력 -->",string2)
