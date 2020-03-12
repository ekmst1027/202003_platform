"""14. 대문자는 소문자로, 소문자는 대문자로 출력하고
영어가 아닌 문자가 입력 되었을 때는 
'입력 형식이 잘못되었습니다' 라고 출력하는 프로그램을 작성하시오."""

import re


def transform(words):
    newWords = ""
    for word in words:
        if word.isupper():
            newWords = newWords + word.lower()
        else:
            newWords = newWords + word.upper()
    print(newWords)


words = input("영어를 입력해주세요 : ")

p = re.compile('[a-zA-z]+')
m = p.match(words)
if(m):
    transform(words)

else:
    print("입력 형식이 잘못되었습니다.")
