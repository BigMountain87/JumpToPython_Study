dic = {'name':'pey','phone':'010-9999-1234','birth':'1118'}


# 딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b'
print(a)

a['name'] = 'pey'
print(a)

# 딕셔너리 요소 삭제하기
del a[1]

print(a)

a = {1:'a',2:'b'}
print(a[1])

print(a[2])

# key 리스트 만들기
a = {'name':'pey','phone':'010-9999-1234','birth':'1118'}
a.keys()

def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
        
    return result

result = two_times([1, 2, 3, 4])
print(result)