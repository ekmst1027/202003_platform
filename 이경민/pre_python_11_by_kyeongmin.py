"""11. 최대공약수를 구하는 함수를 구현하시오"""

# 풀이 의도
# 유클리드 호제법의 원리로 반복문을 사용하여
# 두 수 중 큰 수를 작은 수로 나눈 나머지를 작은 수에 나누는 연산을 반복해 최대공약수를 찾음


def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a


if __name__ == "__main__":
    a = int(input("첫번째 수 : "))
    b = int(input("두번째 수 : "))
    print("최대공약수 :", gcd(a, b))
