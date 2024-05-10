import UtilityFunctions;

class MainProgram:

    """Ask for inputs like $50, $30, $20, $10, $5, $2, $1 in open and closed. Total 12 inputs"""
    
    open_Tickets = []
    close_Tickets = []
    dict_of_Prices = {0: "1", 1: "2", 2: "5", 3: "10", 4: "20", 5: "30", 6: "50"}

    def ask_user_open_tickets(price):
        # Asking for user input for open tickets
        userInput = input(f"${price} tickets in open (type \"exit\" to quit)\n")
        #check for exit
        if UtilityFunctions.isExit(userInput) == True:
            exit(0)
        #return userinput
        return userInput

    def ask_user_close_tickets(price):
        # Asking for user input for close tickets
        userInput = input(f"${price} tickets in close (type \"exit\" to quit)\n")
        #check for exit
        if UtilityFunctions.isExit(userInput) == True:
            exit(0)
        #return userinput
        return userInput
    
    
    
    def main():
        listOfPrices = ["1", "2", "5", "10", "20", "30", "50"]

        #Print Welcome Message
        print("-------------\nWelcome to Lottery Counter!\n-------------")
        print("\nEnter Tickets:")
        print("[Seperate out each ticket using space (ex. 20 21 22 23...) and place \"-\" for empty box or no ticket]\n")
    

        #Get userinput and place in open and close arrays
        for atPrice in listOfPrices:
            #Get open ticket numbers from user in string, convert to array of str, convert to arry of int, then place in open_Ticket array
            temp_open_str_arry = UtilityFunctions.user_string_to_array(MainProgram.ask_user_open_tickets(atPrice))
            temp_open_int_arry = UtilityFunctions.string_arry_to_int_arry(temp_open_str_arry)
            MainProgram.open_Tickets.append(temp_open_int_arry)
           
            #Get close ticket numbers from user in string, convert to array of str, convert to arry of int, then place in open_Ticket array
            temp_close_str_arry = UtilityFunctions.user_string_to_array(MainProgram.ask_user_close_tickets(atPrice))
            temp_close_int_arry = UtilityFunctions.string_arry_to_int_arry(temp_close_str_arry)
            MainProgram.close_Tickets.append(temp_close_int_arry)
        
        #Calculate array of tickets sold for each price and store the array at the index of price
        tickets_at_price = MainProgram.tickets_sold_for_each_price(MainProgram.open_Tickets, MainProgram.close_Tickets)
        #Add up all values in each array in ticket_at_price to get the total number of tickets sold at each price
        total_at_each_price = MainProgram.calc_total_at_each_price(tickets_at_price)
        #Multiply total number of tickets sold at each price to get the amount of money made at each price
        money_at_each_price = MainProgram.getMoneyValue_from_tickets_sold(total_at_each_price)
        #Total every thing to get final total for the amount of money made from selling instant tickets
        total_instant_sell = MainProgram.getTotal_instant_sell(money_at_each_price)
        
        print(total_at_each_price)

   
    
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
                        #Prompt user for help and store user's answer into ticket_sold
                        ticket_sold_string = MainProgram.promptUser_forHelp(price_index + 1, MainProgram.dict_of_Prices.get(price_index), open_ticket_num, close_ticket_num)
                        if UtilityFunctions._string_is_numerical(ticket_sold_string):                     
                            ticket_sold = int(ticket_sold_string)
                        else:
                            #TODO: Prompt user again
                            print("Value conversion error!")
                elif open_ticket_num == "-" and close_ticket_num == "-":
                    ticket_sold = 0
                elif open_ticket_num == "-":
                        #Prompt user for help and store user's answer into ticket_sold
                        ticket_sold_string = MainProgram.promptUser_forHelp(price_index + 1, MainProgram.dict_of_Prices.get(price_index), open_ticket_num, close_ticket_num)
                        if UtilityFunctions._string_is_numerical(ticket_sold_string):                     
                            ticket_sold = int(ticket_sold_string)
                        else:
                            #TODO: Prompt user again
                            print("Value conversion error!")
                        ticket_sold = int(ticket_sold_string)
                elif close_ticket_num == "-": 
                    ticket_sold = open_ticket_num + 1
                arry_of_tickets_sold_at_price.append(ticket_sold)
            arry_tickets_sold_for_each_price.append(arry_of_tickets_sold_at_price)
        return arry_tickets_sold_for_each_price

    def promptUser_forHelp(index, price, open_tick_num, close_tick_num):
        return input(f"Please help me calulate tickets sold for slot {index}, {price}: {open_tick_num} - {close_tick_num} = ")
    
    
    
    def calc_total_at_each_price(tickets_at_price):
        toreturn = []
        #Loop through all the prices
        for price in tickets_at_price:
            priceTotal = 0
            #Loop thorugh each price and add all the sold tickets
            for v in tickets_at_price[price]:
                priceTotal += v
            toreturn.append(priceTotal)
        return toreturn

    def getMoneyValue_from_tickets_sold(ticketSold_at_each_price):
        toreturn = []
        #Loop through each price 
        #[1, 2, 3, 4, 5, 6, 7]
        for (i,v) in enumerate(ticketSold_at_each_price): #i = index, v = value
            money_at_price = v * int(MainProgram.dict_of_Prices[i])
            toreturn.append(money_at_price)
        return toreturn

    def getTotal_instant_sell(money_at_each_price):
        sellTotal = 0
        #Loop thorugh each price and add all the sold tickets
        for v in money_at_each_price:
            sellTotal += v
        return sellTotal

MainProgram.main()
    
