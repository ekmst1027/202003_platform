"""
9. 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
점수를 입력했을 때 해당 학점이 출력되도록 하시오.
81~100 : A
61~80 : B
41~60 : C
21~40 : D
0~20 : F
"""
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
