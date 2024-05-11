import PromptUser
import UtilityFunctions

dict_of_Prices = {0: "1", 1: "2", 2: "5", 3: "10", 4: "20", 5: "30", 6: "50"}


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
                    ticket_sold_string = PromptUser.promptUser_forHelp(price_index + 1, dict_of_Prices.get(price_index), open_ticket_num, close_ticket_num)
                    if UtilityFunctions._string_is_numerical(ticket_sold_string):                     
                        ticket_sold = int(ticket_sold_string)
                    else:
                        #TODO: Prompt user again.
                        print("Value conversion error!")
            elif open_ticket_num == "-" and close_ticket_num == "-":
                ticket_sold = 0
            elif open_ticket_num == "-":
                    #Prompt user for help and store user's answer into ticket_sold
                    ticket_sold_string = PromptUser.promptUser_forHelp(price_index + 1, dict_of_Prices.get(price_index), open_ticket_num, close_ticket_num)
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
        money_at_price = v * int(dict_of_Prices[i])
        toreturn.append(money_at_price)
    return toreturn

def getTotal_instant_sell(money_at_each_price):
    sellTotal = 0
    #Loop thorugh each price and add all the sold tickets
    for v in money_at_each_price:
        sellTotal += v
    return sellTotal
