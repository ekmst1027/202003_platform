"""4. 삼각형의 가로와 높이를 받아서 넓이를 출력하는 함수를 작성하시오."""


def triangleArea(width, height):
    area = width * height / 2
    print(area)


if __name__ == "__main__":
    while(True):
        try:
            width = int(input("삼각형의 가로를 입력하세요 : "))
            height = int(input("삼각형의 가로를 입력하세요 : "))
            triangleArea(width, height)
        except:
            print("숫자를 입력해주세요.")
            continue

        terminator = input("계속 하시겠습니까?(Y)")
        if(terminator != "Y"):
            break
