"""5. N을 입력 받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오(format 활용)"""
dan = int(input("단을 입력해주세요 : "))

for i in range(1, 10):
    print("{} X {} = {}".format(dan, i, dan*i))
