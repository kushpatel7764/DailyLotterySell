class Main:
    """Ask for inputs like $50, $30, $20, $10, $5, $1 in open and closed. Total 12 inputs"""
    
    def ask_user_open_tickets(price):
        # Asking for user input for open tickets
        userInput = input(f"Please provide ${price} tickets in open (please seperate out each ticket using space (ex. 20 21 22 23...)).")
        
        return userInput

    def ask_user_close_tickets(price):
        # Asking for user input for close tickets
        userInput = input(f"Please provide ${price} tickets in close (please seperate out each ticket using space (ex. 20 21 22 23...)).")

        return userInput
