""""2.if문을 이용해 첫번째와 두번 수, 연산기호를 입력하게 하여 계산값이 나오는 계산기를 만드시오"""

# 풀이 의도
# 첫번째 수와 두번째 수를 숫자로 입력하되 숫자가 아닐 경우 예외처리문에 의해 다시 입력값을 받음
# 연산기호는 + , -, *, / , **, % , //를 입력할 수 있으며 각각 연산기호에 대한 결과 값을 프린트
# (나누기의 경우 0을 나눌 경우 예외 발생)
# 계산 후 Y를 입력할 경우 계속 무한루프 실행, 다른 문자 입력 시 종료


def printInitalState():
    print("계산기")
    print("첫번째 수와 두번째 수를 입력한 후 연산기호를 입력해주세요.")
    print("연산기호 종류 : +, -, *, /, **, %, //")
    print("연산기호를 정확하게 입력하여야 하며 0으로 나눌 수 없습니다.")


while(True):
    printInitalState()
    try:
        first_number = int(input('첫번째 수를 입력해주세요 : '))
        second_number = int(input('두번째 수를 입력해주세요 : '))
        operator = input('연산기호를 입력해주세요 : ')
    except:
        print("==============================")
        print("올바른 숫자 및 기호를 입력해주세요")
        print("==============================")
        continue
    if operator == "+":
        print(first_number + second_number)
    elif operator == "-":
        print(first_number - second_number)
    elif operator == "*":
        print(first_number * second_number)
    elif operator == "/":
        try:
            result = first_number / second_number
            print(result)
        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다.")
    elif operator == "**":
        print(first_number ** second_number)
    elif operator == "%":
        print(first_number % second_number)
    elif operator == "//":
        print(first_number // second_number)
    else:
        print("올바른 사칙연산기호를 입력해주세요.")

    terminator = input('계속하시겠습니까?(Y)')
    if terminator != "Y":
        break
