"""3.Enter key를 눌러 주사위를 던지게 한 후, 주사위의 눈이 높은 사람이 승리하는
간단한 주사위 게임을 만드세요"""
from random import randrange

while(True):
    print("주사위 게임")
    input("player1 주사위를 던지세요(Press Enter)")
    first_player = randrange(1, 7)
    print(first_player)
    input("player2 주사위를 던지세요(Press Enter)")
    second_player = randrange(1, 7)
    print(second_player)
    if first_player > second_player:
        print("player1 WIN!!!")
    elif first_player < second_player:
        print("player2 WIN!!!")
    else:
        print("DRAW!!")

    terminator = input("계속 하시겠습니까?(Y)")
    if(terminator != "Y"):
        break
