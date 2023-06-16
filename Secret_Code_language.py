'''
PROGRAM DESCRIPTION:
      WE CAN CONVERT ACTUAL MESSAGE INTO CODE LANGUAGE UNDERSTANDABLE BY OUR INTIMATES. FURTHERMORE:
- WE CAN ALSO RECOVER ACTUAL MESSAGE FROM THE SECRET CODE LANGUAGE 
- TWO PARTS OF THE CODE IS SUMMARIZED AS:-

A) CODING:
-->if the word contains at least 3 characters, remove first character and append it at the end....also append random 3 char at the starting and end of the string
-->else simply reverse the string

B) DECODING:
-->if the word contains less than 3 characters, reverse it
-->else, remove 3 random characters from the starting and end. Now remove te last letter and append it to the first
'''
while True:
    final_msg =[]
    code_decode = input("Enter c to code and d to decode: ").lower()
    if(code_decode == 'c'):        # HERE, WE CONVERT USER INPUT INTO A SECRET CODE LANGUAGE
        a = input("Enter the message to be conveyed: ")
        list_msg = a.split(" ")
        req_string = ""
        req_msg = ""
        for i in range(0, len(list_msg)):
            c = list_msg[i]
            if (len(c)>=3):
                req_string = c[1:len(c)]+ c[0]           # APPENDING FIRST CHARACTER AT THE LAST OF THE STRING
                req_msg = 'mjk' + req_string + 'ijk'     # APPENDING 3 RANDOM CHARACTERS AT THE FIRST AND THE LAST OF STRING
                final_msg.append(req_msg)                # EACH WORD OF THE SENTENCE ARE BEING ADDED TO THE LIST ONE BY ONE
            elif(len(c)<3):
                req_string = c[::-1]                        # REVERSING THE STRING
                final_msg.append(req_string)
        print(" ".join(final_msg))                          # OBTAINING STRING FROM THE LIST
        print()
        try_again = input("PRESS 'y' to try again: ").lower()
        if(try_again == 'y'):
            pass
        else:
            break

    elif(code_decode == 'd'):                 #THIS IS FOR THE PART WHERE WE RECOVER ACTUAL MESSAGE FROM THE SECRET CODE LANGUAGE
        a = input("Enter the message to be decoded: ")
        list_msg1 = a.split(" ")
        req_string = ""
        req_msg = ""
        for i in range(0, len(list_msg1)):
            c = list_msg1[i]
            if(len(c)>=3):
                req_string = c[3:-3]                        #REMOVING FIRST AND LAST 3 RANDOM CHARACTERS
                req_msg = req_string[-1]+req_string[:-1]    #APPENDING LAST CHARACTER TO THE FIRST 
                final_msg.append(req_msg)
            elif(len(c)< 3):
                req_string = c[::-1]
                final_msg.append(req_string)
        print(" ".join(final_msg))                          
        print()
        try_again = input("PRESS 'y' to try again: ").lower()
        if(try_again == 'y'):
            pass
        else:
            break
  
    else:       #THIS STATEMENT IS EXECUTED IF ANY INVALID INPUT IS GIVEN BY THE USER
        print("Invalid input. Please enter only 'c' or 'd'")
        print("\n")
        try_again = input("PRESS 'y' to try again: ").lower()
        if(try_again == 'y'):
            pass
        else:
            break