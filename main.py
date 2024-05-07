class MainProgram:

    """Ask for inputs like $50, $30, $20, $10, $5, $1 in open and closed. Total 12 inputs"""
    
    open_Tickets = []
    close_Tickets = []

    def ask_user_open_tickets(price):
        # Asking for user input for open tickets
        userInput = input(f"Please provide ${price} tickets in open (please seperate out each ticket using space (ex. 20 21 22 23...)).\n")
        
        return userInput

    def ask_user_close_tickets(price):
        # Asking for user input for close tickets
        userInput = input(f"Please provide ${price} tickets in close (please seperate out each ticket using space (ex. 20 21 22 23...)).\n")
        return userInput
    
    def main():
        listOfPrices = ["1", "2", "5", "10", "20", "30", "50"]

        #Print Welcome Message
        print("Welcome to Lottery Counter!")

        for i in listOfPrices:
            MainProgram.open_Tickets.append(MainProgram.ask_user_open_tickets(i))
        print(MainProgram.open_Tickets)

MainProgram.main()
    
