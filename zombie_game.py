import random

def intro():
    print("어느 날, 세계가 좀비로 뒤덮였습니다. 당신은 살아남아야 합니다.")
    print("당신의 선택이 생사를 가릅니다.")
    start_game()

def start_game():
    while True:
        print("\n무엇을 하시겠습니까?")
        print("1. 식량을 찾으러 나간다")
        print("2. 안전한 장소를 찾는다")
        print("3. 좀비와 싸운다")
        print("4. 게임 종료")

        choice = input("선택: ")

        if choice == "1":
            search_food()
        elif choice == "2":
            find_shelter()
        elif choice == "3":
            fight_zombie()
        elif choice == "4":
            print("게임을 종료합니다.")
            break
        else:
            print("올바른 선택이 아닙니다. 다시 선택하세요.")

def search_food():
    outcome = random.choice(["성공", "실패", "위험"])
    if outcome == "성공":
        print("당신은 식량을 찾았습니다!")
    elif outcome == "실패":
        print("아무것도 찾지 못했습니다.")
    else:
        print("좀비에게 쫓기고 있습니다! 어서 도망치세요!")

def find_shelter():
    outcome = random.choice(["안전", "위험"])
    if outcome == "안전":
        print("당신은 안전한 장소를 발견했습니다.")
    else:
        print("이 장소는 이미 좀비들로 가득 차 있습니다! 도망치세요!")

def fight_zombie():
    outcome = random.choice(["승리", "패배"])
    if outcome == "승리":
        print("당신은 용감하게 싸워 좀비를 물리쳤습니다!")
    else:
        print("좀비에게 물리고 말았습니다... 게임 오버.")
        exit()

if __name__ == "__main__":
    intro()
