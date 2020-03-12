"""15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오. 
(리스트 split 과 슬라이싱 활용) """

secure = input("주민번호 13자리를 입력하세요(-로 구분) : ")
behind = secure.split("-")[1]
print(behind[0])
if behind[0] == "1" or behind[0] == "3":
    print("당신은 남자입니다.")
else:
    print("당신은 여자입니다.")
