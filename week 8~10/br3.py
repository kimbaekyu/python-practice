# 1~100까지 더하되 누적 합계(hap)가 1000이상이 되는 시작지점 구하는 프로그램


hap=0

for i in range(1,101):
    hap+=i
    if hap>=1000:
        print(hap)
        break

print("1~100의 합에서 최초로 1000이 넘는 위치 :%d"%i)
