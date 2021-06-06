#dictionary1

student1={'학번':1000,'이름':'고길동','학과':'물리학과'}
student2={'학번':2000,'이름':'둘리','학과':'지질학과'}

print(student1)

student1['연락처']='010-XXXX-XXXX'
print("연락처 추가 : %s"%student1)

student1['학과']='파이썬학과'
print("학과변경 : %s"%student1)

del(student1['이름'])
print("이름 삭제 : %s"%student1)

##값에 접근하는 방법
print(student2['학번'])
print(student2['이름'])
print(student2['학과'])
print(student2.get('학과'))

print("student1의 key : %s"%student1.keys())
print("student1의 key : %s"%list(student1.keys()))

print("student2의 value : %s"%student2.values())
print("student2의 튜플형태 : %s"%student2.items())
print('이름' in student2)
print('연락처' in student2)
