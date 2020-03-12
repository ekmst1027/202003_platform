"""3.Enter key를 눌러 주사위를 던지게 한 후, 주사위의 눈이 높은 사람이 승리하는
간단한 주사위 게임을 만드세요"""
from random import randrange

# 풀이 의도
# Player1과 Player2 순서대로 엔터를 누를 시 1~6값이 랜덤으로 초기화되고 결과가 반환됨
# Y를 입력할 경우 계속 무한루프 실행, 다른 문자 입력 시 종료

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
