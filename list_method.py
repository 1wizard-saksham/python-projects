def teamdiv(li):
    '''
    This is a custom list method. You can import this module and this method called 'teamdiv()' and use it in your program.
    Upon running this function by passing a suitable arguement, you can divide an even group of people into random 2 groups.
    '''
    import random
    if (type(li) is list):
        if len(li) % 2 == 0:
            copy_list = li.copy()
            first_team = random.sample(copy_list, k = int(len(li)/2))
            for i in first_team:
                copy_list.remove(i)
            second_team = random.sample(copy_list, k = int(len(li)/2))
            print(f"first team:- {first_team}, second_team:- {second_team}")
        else:
            print("The list must contain even number of elements")
    else:
        print("Pass list as an arguement")

if __name__ == "__main__":
    teamdiv()
