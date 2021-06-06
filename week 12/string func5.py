# 문자열 함수 활용5

str='Python'
print("str==>",str)
print("str.center(10)==>",str.center(10))
print("str.center(10,'-')==>",str.center(10,'-'))
print("str.ljust(10)==>",str.ljust(10))
print("str.rjust(10)==>",str.rjust(10))
print("str.zfill(10)==>",str.zfill(10))

print("4025는 isdigit(){전체 숫자로만 구성}==>",'4025'.isdigit())
print("soccer는 isalpha(){전체 글자로만 구성}==>",'soccer'.isalpha())
print("7son는 isalnum(){숫자와 글자 섞임 여부}==>",'7son'.isalnum())
print("son heung min은 islower(){전체가 소문자로만 구성}==>",'son heung min'.islower())
print("PARK JI Sung은 isupper(){전체가 대문자로만 구성}==>",'PARK JI Sung'.isupper())
print("' '는 isspace(){전체가 공백문자}==>",' '.isspace())

