"""10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factoral(5)) -> 120 출력"""


def factoral(number):
    if number == 1:
        return 1

    return number * factoral(number-1)


if __name__ == "__main__":
    print(factoral(5))
