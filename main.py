class MainProgram:

    """Ask for inputs like $50, $30, $20, $10, $5, $1 in open and closed. Total 12 inputs"""
    
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
            #Get open ticket numbers from user in string, convert to array, then place in open_Ticket array
            temp_open = MainProgram.user_string_to_array(MainProgram.ask_user_open_tickets(atPrice))
            MainProgram.open_Tickets.append(temp_open)
           
            #Get close ticket numbers from user in string, convert to array, then place in open_Ticket array
            temp_close = MainProgram.user_string_to_array(MainProgram.ask_user_close_tickets(atPrice))
            MainProgram.close_Tickets.append(temp_close)
        #Convet arrays of string to arrays of ints
        
        #Calculate total tickets sold for each price and store the total at the index of price
        tickets_at_price = MainProgram.tickets_sold_for_each_price(MainProgram.open_Tickets, MainProgram.close_Tickets)

        
        print(MainProgram.open_Tickets)

    def user_string_to_array(userInput):
        temp_string = userInput.strip()
        temp_array = temp_string.split(" ")

        return temp_array

    def tickets_sold_for_each_price(open_Tickets, close_Tickets):
        #Length of tickets should be same at each index for both open and close -- check this later
        for price in range(6): #Six input for 50, 30, 20, 10, 5, 2, 1 tickets, Loop through all the prices
            #For each price iterate through open and close list to calculate subtraction
            pass
        pass


MainProgram.main()
    
