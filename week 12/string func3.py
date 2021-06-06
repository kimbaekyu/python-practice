# 문자열 함수 활용3

str='Study python'
print("원래 문자열==>",str)
print("str.split==>",str.split())
print("---------------------------------")

str2='ONE:TWO:THREE'
print("원래 문자열 ==>",str2)
print("str2.split(':')==>",str2.split(':'))
print("---------------------------------")
str3='one\ntwo\nthree'
print("원래 문자열\n",str3)
print("str3.splitlines()==>",str3.splitlines())
print("---------------------------------")
str4='#'
print("원래 문자열==>",str4)
print("str4.join('파이썬')==>",str4.join('파이썬'))
