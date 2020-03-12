"""10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factoral(5)) -> 120 출력"""

# 풀이 의도
# 재귀용법을 사용해 인자가 1이 될때까지 계속 값을 곱하며 인자가 1일 경우 1을 리턴함


def factoral(number):
    if number == 1:
        return 1

    return number * factoral(number-1)


if __name__ == "__main__":
    print(factoral(5))
