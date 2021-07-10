import random
pl_pos = 1
com_pos = 1


def board():
    print("○" * (pl_pos - 1) + "P" + "○" * (30 - pl_pos) + "Goal")
    print("○" * (com_pos - 1) + "C" + "○" * (30 - com_pos) + "Goal")


board()
print("주사위 게임 스타트!!")
while True:
    input("Enter를 누르면 주사위를 굴립니다.")
    role_the_dice = random.randint(1, 6)
    print("------------------------------------------------------------------")
    print("플레이어 주사위 눈의 숫자가 " + str(role_the_dice) + " 이(가) 나왔습니다.")
    pl_pos = pl_pos + role_the_dice
    if pl_pos > 30:
        pl_pos = 30
    board()
    if pl_pos == 30:
        print("플레이어의 승리!")
        break

    input("Enter를 누르면 컴퓨터의 말을 굴립니다.")
    role_the_dice = random.randint(1, 6)
    print("------------------------------------------------------------------")
    print("컴퓨터 주사위 눈의 숫자가 " + str(role_the_dice) + " 이(가) 나왔습니다.")
    com_pos = com_pos + role_the_dice
    if com_pos > 30:
        com_pos = 30
    board()
    if com_pos == 30:
        print("컴퓨터의 승리!")
        break


