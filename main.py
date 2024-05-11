import UtilityFunctions
import PromptUser
import Calculations
import os.path #Is used to check if a file exists or not

path = "./previous_day_close_data" #Path to the file, which I want to check if it exists or not. 

def _does_file_exists(path):
    if os.path.isfile(path):
        return True
    else:
        return False

class MainProgram:

    """Ask for inputs like $50, $30, $20, $10, $5, $2, $1 in open and closed. Total 12 inputs"""
    
    open_Tickets = []
    close_Tickets = []
    
    def main():
        listOfPrices = ["1", "2", "5", "10", "20", "30", "50"]

        #Print Welcome Message
        print("-------------\nWelcome to Lottery Counter!\n-------------")
        print("\nEnter Tickets:")
        print("[Seperate out each ticket using space (ex. 20 21 22 23...) and place \"-\" for empty box or no ticket]\n")
    

        #Get userinput and place in open and close arrays
        for atPrice in listOfPrices:
            #Only want to ask user for open input, if no previous day close data is dectected. 
            if (_does_file_exists(path) and len(MainProgram.open_Tickets) < 1):
                MainProgram.open_Tickets.append("Nothing")
            else:
                #Get open ticket numbers from user in string, convert to array of str, convert to arry of int, then place in open_Ticket array
                temp_open_str_arry = UtilityFunctions.user_string_to_array(PromptUser.ask_user_open_tickets(atPrice))
                temp_open_int_arry = UtilityFunctions.string_arry_to_int_arry(temp_open_str_arry)
                MainProgram.open_Tickets.append(temp_open_int_arry)
           
            #Get close ticket numbers from user in string, convert to array of str, convert to arry of int, then place in open_Ticket array
            temp_close_str_arry = UtilityFunctions.user_string_to_array(PromptUser.ask_user_close_tickets(atPrice))
            temp_close_int_arry = UtilityFunctions.string_arry_to_int_arry(temp_close_str_arry)
            MainProgram.close_Tickets.append(temp_close_int_arry)
        
        #Calculate array of tickets sold for each price and store the array at the index of price
        tickets_at_price = Calculations.tickets_sold_for_each_price(MainProgram.open_Tickets, MainProgram.close_Tickets)
        #Add up all values in each array in ticket_at_price to get the total number of tickets sold at each price
        total_at_each_price = Calculations.calc_total_at_each_price(tickets_at_price)
        #Multiply total number of tickets sold at each price to get the amount of money made at each price
        money_at_each_price = Calculations.getMoneyValue_from_tickets_sold(total_at_each_price)
        #Total every thing to get final total for the amount of money made from selling instant tickets
        total_instant_sell = Calculations.getTotal_instant_sell(money_at_each_price)
        
        print(total_at_each_price)

   
    
 
MainProgram.main()
    
