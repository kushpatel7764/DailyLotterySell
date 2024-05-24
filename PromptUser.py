import UserExit

def ask_user_tickets(price, time):
        userInput = []
        row_num = 1
        keepGoing = True
        # Asking for user input for open tickets
        print(f"Time: {time}") #time is only "open" and "close"
        print(f"Enter ticket numbers of each ${price} ticket: ")
        while keepGoing:
            row_val  = input(f"{row_num}. ")
            #check for exit 
            if UserExit.isExit(row_val) == True:
                exit(0)
            #if used pressed enter
            if row_val == "":
                 keepGoing = False
            else: 
                userInput.append(row_val)
                row_num += 1
        #return userinput
        return userInput

def promptUser_forHelp(index, price, open_tick_num, close_tick_num):
    return input(f"Please help me calulate tickets sold for slot {index}, ${price}: {open_tick_num} - {close_tick_num} = ")

