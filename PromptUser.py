import UserExit
from colorama import Fore

def ask_user_open_tickets(price):
        # Asking for user input for open tickets
        userInput = input(f"${price} tickets in {Fore.BLUE}open{Fore.WHITE} (type \"exit\" to quit)\n")
        #check for exit
        if UserExit.isExit(userInput) == True:
            exit(0)
        #return userinput
        return userInput

def ask_user_close_tickets(price):
    # Asking for user input for close tickets
    userInput = input(f"${price} tickets in {Fore.RED}close{Fore.WHITE} (type \"exit\" to quit)\n")
    #check for exit
    if UserExit.isExit(userInput) == True:
        exit(0)
    #return userinput
    return userInput

def promptUser_forHelp(index, price, open_tick_num, close_tick_num):
    return input(f"Please help me calulate tickets sold for slot {index}, {price}: {open_tick_num} - {close_tick_num} = ")



    