class MainProgram:

    """Ask for inputs like $50, $30, $20, $10, $5, $2, $1 in open and closed. Total 12 inputs"""
    
    open_Tickets = []
    close_Tickets = []

    def ask_user_open_tickets(price):
        # Asking for user input for open tickets
        userInput = input(f"${price} tickets in open (type \"exit\" to quit)\n")
        #check for exit
        if MainProgram.isExit(userInput) == True:
            exit(0)
        #return userinput
        return userInput

    def ask_user_close_tickets(price):
        # Asking for user input for close tickets
        userInput = input(f"${price} tickets in close (type \"exit\" to quit)\n")
        #check for exit
        if MainProgram.isExit(userInput) == True:
            exit(0)
        #return userinput
        return userInput
    
    def isExit(input):
        if input == "exit":
            return True
        else: 
            return False
    
    def main():
        listOfPrices = ["1", "2", "5", "10", "20", "30", "50"]

        #Print Welcome Message
        print("-------------\nWelcome to Lottery Counter!\n-------------")
        print("\nEnter Tickets:")
        print("[Seperate out each ticket using space (ex. 20 21 22 23...) and place \"-\" for empty box or no ticket]\n")
    

        #Get userinput and place in open and close arrays
        for atPrice in listOfPrices:
            #Get open ticket numbers from user in string, convert to array of str, convert to arry of int, then place in open_Ticket array
            temp_open_str_arry = MainProgram.user_string_to_array(MainProgram.ask_user_open_tickets(atPrice))
            temp_open_int_arry = MainProgram.string_arry_to_int_arry(temp_open_str_arry)
            MainProgram.open_Tickets.append(temp_open_int_arry)
           
            #Get close ticket numbers from user in string, convert to array of str, convert to arry of int, then place in open_Ticket array
            temp_close_str_arry = MainProgram.user_string_to_array(MainProgram.ask_user_close_tickets(atPrice))
            temp_close_int_arry = MainProgram.string_arry_to_int_arry(temp_close_str_arry)
            MainProgram.close_Tickets.append(temp_close_int_arry)
        
        #Calculate array of tickets sold for each price and store the array at the index of price
        tickets_at_price = MainProgram.tickets_sold_for_each_price(MainProgram.open_Tickets, MainProgram.close_Tickets)
        #Add up each array in ticket_at_price to get told number of tickets sold at each price
        #Multiply total number of tickets sold at each price to get the amount of money made at each price
        #Total every thing to get final total for the amount of money made from selling instant tickets
        
        print(MainProgram.open_Tickets)

    def user_string_to_array(userInput):
        #strip() - will remove leading and trailing white spaces
        temp_string = userInput.strip()
        temp_array = temp_string.split(" ")
        return temp_array
    
    def string_arry_to_int_arry(str_arry):
        """
        This function requires that open_Tickets and close_Tickets be an array with an array of strings inside.
        string_arry_to_int_arry will given array of str to array of int. 
        """
        to_return = []
        for v in str_arry:
            if v.isdigit():
                to_return.append(int(v))
            elif v == "-":
                to_return.append(v)
            else:
                print("Invalid character detected. Quitting the program now...")
                exit(0)
        return to_return

    def tickets_sold_for_each_price(open_Tickets, close_Tickets):
        arry_tickets_sold_for_each_price = []
        #Length of tickets should be same at each index for both open and close -- check this later
        for price_index in range(7): #Six input for 50, 30, 20, 10, 5, 2, 1 tickets, Loop through all the prices
            arry_of_tickets_sold_at_price = []
            #For each price iterate through open or close list to calculate subtraction, length of open or close should be same so it does not matter which one is being iterated.
            for i,open_ticket_num in enumerate(open_Tickets):
                close_ticket_num = close_Tickets[i]
                #Subtract number from open with number from close to get how many tickets were sold
                #Work with nil 
                if open_ticket_num != "-" and close_ticket_num != "-":
                    if open_ticket_num > close_ticket_num:
                        ticket_sold = open_ticket_num - close_ticket_num
                    else:
                        #Prompt user
                        pass
                elif open_ticket_num == "-" and close_ticket_num == "-":
                    ticket_sold = 0
                elif open_ticket_num == "-":
                    #Prompt user
                    pass
                elif close_ticket_num == "-":
                    ticket_sold = open_ticket_num + 1
                arry_of_tickets_sold_at_price.append(ticket_sold)
            arry_tickets_sold_for_each_price.append(arry_of_tickets_sold_at_price)
        return arry_tickets_sold_for_each_price


MainProgram.main()
    
