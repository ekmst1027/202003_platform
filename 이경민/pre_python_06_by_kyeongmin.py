"""6. 아래와 같이 별이 찍히게 출력하시오.
숫자를 입력하세요 : 5
    ★
   ★★
  ★★★
 ★★★★
★★★★★
 ★★★★
  ★★★
   ★★
    ★
"""

# 풀이 의도
# 숫자를 입력할 시, 공백과 별의 갯수를 조합하여 위의 모양대로 나오도록 출력함
# ex)
# 입력) 숫자를 입력하세요: 3
# 출력)
# ★
# ★★
# ★★★
# ★★
# ★

number = int(input("숫자를 입력하세요 : "))
for i in range(number*2):
    if(i < number):
        for j in range(number - i - 1):
            print(" ", end="")
        for j in range(i+1, 0, -1):
            print("★", end="")
        print()
    else:
        for j in range(i - number + 1):
            print(" ", end="")
        for j in range(number*2 - i - 1):
            print("★", end="")
        print()
