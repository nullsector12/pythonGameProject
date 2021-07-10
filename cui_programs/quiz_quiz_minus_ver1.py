"""
퀴즈 게임 ver.1
o/x 퀴즈

1. 문제
2. 정답
3. 플레이어의 답안 입력
4. 답안과 정답 비교
5. 정답/오답 표시

"""

# 문제집
# 배열을 사용하여 문제 생성
question = ["한복은 한국 고유의 의복양식이다.", "김치는 한국 고유의 발효 음식이다.", "이순신 장군이 전사한 해전은 명량해전이다."]
answer = ["o", "o", "x"]

if __name__ == '__main__':

    # 문제 개수만큼 반복하기
    for index in range(len(question)):
        print(">>>>>>>> 문제 " + str(index+1) + "번 <<<<<<<<<")
        print(question[index])
        print("맞으면 O , 틀리면 X 를 입력해주세요.")
        # 플레이어가 입력한 정답
        ans = input()
        if ans == answer[index]:
            print("#####################")
            print("##### 정답입니다! #####")
            print("#####################")
        else:
            print("######################")
            print("#### 이걸 틀리네... ####")
            print("######################")

