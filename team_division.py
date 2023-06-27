"""THIS IS A PROGRAM THAT DIVIDES A GROUP OF EVEN(2,4,6,8,.........) PEOPLE INTO DIFFERENT GROUPS"""
def team_division():
    import random
    list_to_be_divided =[]

    while True:
            user_input = input("Enter the even no of players you want the group of: ")
            try:
                if (int(user_input) % 2 == 0):
                    break
                else:
                    print("Please enter only the even number of players. At least 2 required")
            except ValueError:
                print("Please enter integer value")

    item = 1

    while True:
        players = input(f"Enter player {item}: ")
        if players.isnumeric():
            print("Please enter string only, not digits or any other special symbols")
            continue
        else:
            list_to_be_divided.append(players)
            item += 1
        if (len(list_to_be_divided) == user_input):
            break

    copy_list_to_be_divided = list_to_be_divided.copy()

    first_team = random.sample(copy_list_to_be_divided, k = int(user_input/2))
    
    for i in first_team:
        copy_list_to_be_divided.remove(i)

    second_team = random.sample(copy_list_to_be_divided, k = int(user_input/2))
    print(f"The first team is:-{first_team}\nThe second team is:-{second_team}")

if __name__ == "__main__":
    team_division()