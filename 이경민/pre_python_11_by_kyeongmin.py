"""11. 최대공약수를 구하는 함수를 구현하시오"""


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
