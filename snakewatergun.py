def snake_water_gun():
    '''
    THIS IS A SNAKE, WATER AND GUN GAME. SOME APPROACHES MIGHT BE DIFFERENT. HOWEVER, THE PROGRAM IS USER-FRIENDLY AND I BELIEVE YOU WON'T BE HAVING ANY PROBLEMS.
    '''
    import random
    import time
    print("SNAKE, WATER, GUN GAME".center(65))
    print()
    choices = ['snake', 'water', 'gun']
    print(f"The list of choices is:- {choices}\n")
    user_point = 0
    computer_point = 0

    while True:
        computer_chose = []
        check_invalid = True
        n =1
        try:
            rounds = int(input("enter the number of rounds you want to play:- "))
            print()
            for i in range(rounds):
                user_choice = input(f"Please Enter Your Choice {n}:- ").lower()
                print()
                print(f"Computer is selecting it's choice {n} ...... ........\n")
                time.sleep(2)
                computer_choice = random.choice(choices)
                computer_chose.append(computer_choice)
                if user_choice in choices:
                    if user_choice == 'snake' and computer_choice == 'water':
                        user_point += 1
                    elif user_choice == 'snake' and computer_choice == 'gun':
                        computer_point += 1
                    elif user_choice == 'water' and computer_choice == 'gun':
                        user_point +=1
                    elif user_choice == 'water' and computer_choice == 'snake':
                        computer_point += 1
                    elif user_choice == 'gun' and computer_choice == 'water':
                        computer_point+=1
                    elif user_choice == 'gun' and computer_choice == 'snake':
                        user_point+=1
                    else:
                        pass
                else:
                    check_invalid = False
                    print("Invalid input")
                    break
                n += 1
            if check_invalid:
                print(f'Computer choice:- {computer_chose}')
                print()
                print(f"EVALUATION:- The Computer's point is {computer_point} and your point is {user_point}")
                if(user_point > computer_point):
                    print("So, you win. Congratulations!!\n")
                else:
                    print("So, you lose.\n")

        except ValueError:
            print("Unexpected value...Please Enter an integer")
            print()

        finally:
            try_again = input("Press 'y' to try again or press any key to exit: ").lower()
            if try_again == 'y':
                print()
            else:
                break

if __name__ == "__main__":
    snake_water_gun()