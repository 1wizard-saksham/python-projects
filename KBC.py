print("WELCOME KO KBC(KAUN BANEGA CROREPATI)".center(90), "\n")
chk = False
m =1
answer_count = 0
#CREATING THE QUESTION AND ANSWER LIST(There questions in index 0 of every items whereas answers in index 1 of all items with 5 items in total)
li =[
    ['''A. In which among the following organ, “Bowman’s Capsule” is found?
        1. Liver                   2. Kidney
        3. Heart                   4. Small intestine''', '2'],
    ['''B. Corpus Callosum makes an important part of which among the following organs in Human body?
        1. Brain                    2. Liver              
        3. Kidney                   4. Spinal cord''', '1'],
    ['''C. Out of Diphtheria, Whooping cough, Typhoid , Diarrhea & Malaria which is not caused by bacteria?
        1. Whooping Cough                  2. Malaria
        3. Typhoid                         4. None of the above''', '2'],
    ['''D. Which among the following is called ‘queen of spices’?
        1. Cardamom                    2. Turmeric
        3. Clove                       4. None of the above''', '1'],
    ['''E. The edible part of ‘cabbage’ is which of the following?
        1. Inflorescence                   2. fruit
        3. Bud                             4. none of the above''', '3']
]
print('''You'll be asked five questions and the prize for each of the questions are listed below:-
    ** For 1st question: 5 lakh
    ** For 2nd qn: 10 lakh
    ** For 3rd qn: 20 lakh
    ** For 4th qn: 40 lakh
    ** For 5th qn: 1 crore ''', "\n")
#Looping through the elements of the list
for i in range(0, 5):
    print("Question ", m," is:\n", li[i][0], "\n")
    answer_key = input("Enter your answer(1-4): ") #Asking the user to input their answer
    real_answer = li[i][1]
    # Checking all the required conditions
    if (answer_key == real_answer):
        answer_count+=1
        if(answer_count == 1):
            print()
            print("You just won 5 lakh rupees\n")
        elif(answer_count == 2):
            print()
            print("You just won 10 lakh rupees\n")
        elif(answer_count == 3):
            print()
            print("You just won 20 lakh rupees\n") 
        elif(answer_count == 4):
            print()
            print("You just won 40 lakh rupees. But, if you don't answer another question you'll lose all you money ")
            check = input("Enter y to continue and n to exit: ").lower()
            if (check != 'y'):
                chk = True  #Changing the value of the boolean
                break
            else:
                pass
        elif(answer_count == 5):
            print()
            print("CONGRATULATIONS TO BE A CROREPATI. YOU WON 1 CRORE RUPEES!!!!!!")
    else:
        if(answer_count < 1):
            print()
            print("WRONG ANSWER..... You don't win anything")
            break
        elif(answer_count < 2):
            print()
            print("WRONG ANSWER.....In aggregate, You win only 5 lakh rupees")
            break
        elif(answer_count < 3):
            print()
            print("WRONG ANSWER.....In aggregate, You win only 10 lakh rupees")
            break
        elif(answer_count < 4):
            print()
            print("WRONG ANSWER.....In aggregate, you win only 20 lakh rupees")
        elif(answer_count < 5):
            print()
            print("Sorry, you lost all your money")
    m +=1
#Loop will break and the program will be directed here if the user presses 'n'
if(chk):
    print("Congratulations for wining 40 lakh rupees")