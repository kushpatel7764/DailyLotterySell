import UtilityFunctions
import PromptUser
import Calculations
import TableOutput_Management
from colorama import Fore
import ErrorHandling

#TODO: Get scanner working 
    #TODO: When user prompted for help, give vaild GameNumber as well
    #TODO: Excel Output
#TODO: Save to open from previous day's close
class MainProgram:

    """Ask for inputs like $50, $30, $20, $10, $5, $2, $1 in open and closed. Total 12 inputs"""
    
    open_Tickets = []
    close_Tickets = []
    
    def main():
        listOfPrices = ["50", "30", "20", "10", "5", "2", "1"]

        #Print Welcome Message
        print("-------------\nWelcome to Lottery Counter!\n-------------")
        print("\nEnter Tickets:")
        print("[Seperate out each ticket using space (ex. 20 21 22 23...) and place \"-\" for empty box or no ticket]\n")

        #Get userinput and place in open and close arrays
        atPrice = 0
        while atPrice < 7:
            #Get open ticket numbers from user in string, convert to array of str, convert to arry of int, then place in open_Ticket array
            temp_open_str_arry = UtilityFunctions.user_string_to_array(PromptUser.ask_user_open_tickets(listOfPrices[atPrice]))
            #Allows user to go to previous price if the user enters "p" at index 0.
            if temp_open_str_arry[0] == "p":
                if atPrice > 0:
                    atPrice -= 1
                continue
            temp_open_int_arry = UtilityFunctions.string_arry_to_int_arry(temp_open_str_arry)
            

            #Get close ticket numbers from user in string, convert to array of str, convert to arry of int, then place in open_Ticket array
            temp_close_str_arry = UtilityFunctions.user_string_to_array(PromptUser.ask_user_close_tickets(listOfPrices[atPrice]))
            #Allows user to go to previous price if the user enters "p" at index 0.
            if temp_close_str_arry[0] == "p":
                if atPrice > 0:
                    atPrice -= 1 
                continue
            temp_close_int_arry = UtilityFunctions.string_arry_to_int_arry(temp_close_str_arry)


            #If the user puts the same amount of inputs for a price then append else rerun the same price
            if (ErrorHandling.check_user_input_size(temp_open_int_arry, temp_close_int_arry)):
                MainProgram.open_Tickets.append(temp_open_int_arry)
                MainProgram.close_Tickets.append(temp_close_int_arry)
                atPrice += 1
            else:
                print("Error open and close sizes do not match at price!")

        
        #Calculate array of tickets sold for each price and store the array at the index of price. 
        tickets_at_price = Calculations.tickets_sold_for_each_price(MainProgram.open_Tickets, MainProgram.close_Tickets) #Sell
        #Add up all values in each array in ticket_at_price to get the total number of tickets sold at each price
        total_at_each_price = Calculations.calc_total_at_each_price(tickets_at_price) 
        #Multiply total number of tickets sold at each price to get the amount of money made at each price
        money_at_each_price = Calculations.getMoneyValue_from_tickets_sold(total_at_each_price)
        #Total every thing to get final total for the amount of money made from selling instant tickets
        total_instant_sell = Calculations.getTotal_instant_sell(money_at_each_price)

        #Convert open_Tickets, close_Tickets, sell to string
        open = []
        close = []
        sell = []
        for price in range(7):
            #convert open_Tickets
            open.append(UtilityFunctions.int_arry_to_string_arry(MainProgram.open_Tickets[price]))
            #convert close_Tickets
            close.append(UtilityFunctions.int_arry_to_string_arry(MainProgram.close_Tickets[price]))
            #convert total_at_each_price - sell_arry
            sell.append(UtilityFunctions.int_arry_to_string_arry(tickets_at_price[price]))


        
        table = TableOutput_Management.TableOutput(open, close, sell, total_instant_sell)
        table.Terminal_Output()

        

        
    
 
MainProgram.main()
    
