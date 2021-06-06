#문자열 함수 활용 6
while(1):

    test=input("숫자 혹은 문자를 입력해주세요[끝내려면 끝을 입력하세요.] : ")

    if test=='끝':
        print("프로그램을 종료합니다.")
        break
    
    elif test.isdigit()==True:
        print("전체가 숫자로 구성되어 있습니다.")

    elif test.isalpha()==True:
        print("전체가 글자로 구성되어 있습니다.")

    elif test.isalnum()==True:
        print("숫자와 글자가 섞여 있습니다.")

    elif test.islower()==True:
        print("전체가 소문자로 구성되어 있습니다.")

    elif test.isupper()==True:
        print("전체가 대문자로 구성되어 있습니다.")

    elif test.isspace()==True:
        print("전체가 공백문자로 구성되어 있습니다.")
    
