import random
import datetime
ALP = ["A", "B", "C", "D", "E", "F", "G",
       "H", "I", "J", "K", "L", "M", "N",
       "O", "P", "Q", "R", "S", "T", "U",
       "V", "W", "X", "Y", "Z"]
r = random.choice(ALP)
alp = ""
for i in ALP:
    if i != r:
        alp = alp + i
print(alp)
st = datetime.datetime.now()
ans = input("빠진 알파벳은 무엇?")
if ans.upper() == r:
    print("정답입니다!")
    et = datetime.datetime.now()
    print("풀이까지 총 "+ str((et-st).seconds) + "초 소요")
else:
    et = datetime.datetime.now()
    print("풀이까지 총 " + str((et-st).seconds) + "초 소요")
    print("오답입니다!")