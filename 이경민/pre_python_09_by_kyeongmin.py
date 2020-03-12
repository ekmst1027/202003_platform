"""
9. 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
점수를 입력했을 때 해당 학점이 출력되도록 하시오.
81~100 : A
61~80 : B
41~60 : C
21~40 : D
0~20 : F
"""

# 풀이 의도
# python에서는 switch-case문이 없기 때문에 비슷하게 사용할 수 있는 dictionary 자료구조를 사용
# 0~100점의 점수를 10으로 나눈 뒤 소수점은 다 올려서 학점으로 계산

import math

score = int(input("점수를 입력하세요 : "))
changed_score = math.ceil(score / 10)
grade = {
    10: 'A',
    9: 'A',
    8: 'B',
    7: 'B',
    6: 'C',
    5: 'C',
    4: 'D',
    3: 'D',
    2: 'F',
    1: 'F',
    0: 'F'
}
print("당신의 학점은 {}입니다.".format(grade[changed_score]))
