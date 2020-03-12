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
