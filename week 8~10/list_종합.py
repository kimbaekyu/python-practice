# 리스트 종합

list=[11,10,20]
print("현재 리스트:%s"%list)

list.append(40)
print("append(40)후의 리스트 : %s"%list)

print("pop()으로 추출한 값:%s"%list.pop())
print("pop()후의 리스트 : %s"%list)

list.reverse()
print("reverse()후의 리스트 : %s"%list)

print("20값의 위치:%d"%list.index(20))

list.insert(2,223)
print("insert(2,223)후의 리스트 : %s"%list)

list.remove(223)
print("remove(223)후의 리스트: %s"%list)

list.extend([11,22,33])
print("extend([11,22,33])후의 리스트: %s"%list)

print("11값의 개수:%d"%list.count(11))
