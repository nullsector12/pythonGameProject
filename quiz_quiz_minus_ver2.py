"""

퀴즈 게임 ver.2

1. 장르의 선택
2. 주관식과 객관식 문제의 추가와 관련 로직 추가
3. 게임 종료시, 푼 문제의 갯수와 점수 표시

"""

# 문제집
# 1. 장르와 장르별 퀴즈 생성 / 주관식과 객관식, ox 문제 분리
# Hash 구조 사용
# Hash 내부에 새로운 Hash를 담아 문제의 스타일을 key값으로 세팅
genre = {"1": {"주관식": "실시간 전략게임의 약어는 OOO Game 이다.",
               "객관식": "\"VR 게임\"에서 \"VR\"은 무엇을 줄인 말인지 보기에서 고르시오",
               "ox": "한국 최초의 PC 온라인게임은 바람의 나라이다."},

         "2": {"객관식": "한국 최초의 1000만 영화는 무엇인지 보기에서 고르시오",
               "ox": "봉준호 감독의 작품 \"기생충\"이 아카데미에서 수상한 부문은 6개다.",
               "주관식": "2004년작 영화 \"노트북\" 속 주인공들의 이름은 노엘과 OO이다."},

         "3": {"ox": "이순신 장군이 전사한 전투는 노량해전이다.",
               "주관식": "을사늑약(을사조약)이 일어난 년도는 OOOO년 이다.",
               "객관식": "임진왜란이 발발한 년도를 보기에서 고르시오."}}

genre_answer = {"1": {"주관식": "RTS", "ox": "x", "객관식": "4"},
                "2": {"주관식": "엘리", "ox": "x", "객관식": "2"},
                "3": {"주관식": "1905", "ox": "o", "객관식": "1"}}


# 2. 플레이어가 게임 장르를 선택 가능
def choice_genre(select):
    correct = 0
    keys = genre.get(select).keys()

    if select == "1":
        print("장르 : 게임을 선택하셨습니다.")
        for key in keys:
            answer = genre_answer.get(select).get(key)
            if key == "객관식":
                print(genre.get(select).get(
                    key) + "\n 1. Visual Reality \n 2. Vision Revolution \n 3. Virtual Revolution \n 4. Virtual Reality")
                correct += check_answer(answer)
            else:
                print(genre.get(select).get(key))
                correct += check_answer(answer)
    elif select == "2":
        print("장르 : 영화를 선택하셨습니다.")
        for key in keys:
            answer = genre_answer.get(select).get(key)
            if key == "객관식":
                print(genre.get(select).get(
                    key) + "\n 1. 쉬리 \n 2. 실미도 \n 3. 친구 \n 4. 클래식")
                correct += check_answer(answer)
            else:
                print(genre.get(select).get(key))
                correct += check_answer(answer)
    elif select == "3":
        print("장르 : 한국사를 선택하셨습니다.")
        for key in keys:
            answer = genre_answer.get(select).get(key)
            if key == "객관식":
                print(genre.get(select).get(
                    key) + "\n 1. 1592 \n 2. 1593 \n 3. 1594 \n 4. 1595")
                correct += check_answer(answer)
            else:
                print(genre.get(select).get(key))
                correct += check_answer(answer)

    # 3. 게임이 모두 끝났을 때, 문제를 푼 갯수와 점수를 표시함
    print("맞힌 문제 : " + str(correct) + " / " + "점수 : " + str(correct * 10))


# 반복되는 정답 대조 기능을 하나의 함수로 분리
def check_answer(answer):
    player_answer = input().upper()
    if player_answer == answer.upper():
        print("정답입니다! +10점")
        return 1

    else:
        print("오답입니다!")
        return 0


if __name__ == '__main__':

    print("문제 장르를 선택해주세요. \n[1] 게임 \n[2] 영화 \n[3] 한국사")
    select_genre = input()
    choice_genre(select_genre)

