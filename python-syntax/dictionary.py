# dictionary 

dic = {}
dic["dictionary"] = "aaa"
dic["python"] = "123132"
dic['dictionary'] 
print(dic)

del dic['python']
print(dic)
# 문자열, 리스트, 튜플은 인덱스를 이용해서 값을 조회하는데, 딕셔너리는 키를 이용하는 것이 큰 차이점이다. 
# 또 딕셔너리 자료형은 해싱(hasing)기법을 이용하기 때문에 자료가 순서대로 저장되지 않는다. 

family = {'boy': 'choi', 'girl': 'kim', 'baby': 'choi'}
print(family)
print(family.keys())
print(family.values())
# 키값이 있는지 없는지 확인하기
print('boy' in family)
print('aa' in family)

# 연습문제 
def korean_number(num):
    dic = {1: "일", 2: "이", 3: "삼", 4: "샤", 5: "오", 6: "육", 7: "칠", 8: "팔", 9: "구"}
    return dic[num]

print(korean_number(2))