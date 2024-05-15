"""
    TableOutput class provides methods to handle different types of outputs (terminal, text, Excel) for 
    filtered meteorite data.

    Attributes:
    - outputTypeChosen (str): Represents the user's choice for the type of output.
    - sortedList (list): the sorted list of meteorite objects.
"""

import xlwt
import UtilityFunctions
from colorama import Fore
from Calculations import dict_of_Prices



class TableOutput:
    def __init__(self,  open, close, sell, instantTotal):
        """
        Initializes a TableOutput object.
        """
        self.row_Number = 1 # The number of the row in the terminal table output
        self.open = open
        self.close = close
        self.sell = sell   
        self.instantTotal = instantTotal
        self.price = 0


    def fortmated_Table(self, tableString = ""):

        print("\n")
        tableString = tableString + TableOutput.Create_Terminal_Row_Label() + "\n"
        tableString = tableString + TableOutput.Draw_Terminal_Table_Sepration_Line(50) + "\n"
        for price in range(7):
            #For each price create a label
            self.price = dict_of_Prices[price]
            
            #Create row of data for each price
            for row, value in enumerate(self.open[price]):
                tableString = tableString + TableOutput.Create_Terminal_Data_Row(self, price, row) + "\n" 
            tableString = tableString + TableOutput.Draw_Terminal_Table_Sepration_Line(50) + "\n"
        return tableString

    def Draw_Terminal_Table_Sepration_Line(lineLength, line = ""):
        """
        Draws a separation line for the terminal table.

        Parameters:
        - lineLength (int): The length of the separation line.
        - line (str): A string to accumulate the separation line.

        Returns:
        - The separation line string.
        """

        for i in range(lineLength):
            if (i == (lineLength-1)):
                line = line + "=\n"
                break
            line = line + "="
        return line

    def Create_Terminal_Row_Label():
        """
        Creates the label row for the terminal table.

        Returns:
        - A formatted string of row labels.
        """

        labels = ["#","PRICE" ,"OPEN", "CLOSE", "SELL"]
        return TableOutput.setup_Terminal_Row(labels)
        
    
    def Create_Terminal_Data_Row(self, price, lineNum):
        """
        Creates a data row for the terminal table.

        Parameters:
        - lineNum (int): The line number of the row.
        - sortedObj: An object containing data to be displayed.

        Returns:
        - A formatted string of data for a single row.
        """

        toReturn = ""
        lineInfo = [str(self.row_Number), dict_of_Prices[price],self.open[price][lineNum], self.close[price][lineNum], self.sell[price][lineNum]] #+1 is added to convert from index to number
        self.row_Number += 1
        toReturn = TableOutput.setup_Terminal_Row(lineInfo, toReturn)
        return toReturn
    
    def setup_Terminal_Row(lineInfo, toAppendReturn = ""):
        """
        Sets up a row for the terminal table given information about what to put in the row.

        Parameters:
        - lineInfo (list): List of data to be displayed in a row.
        - toAppendReturn (str): A string to accumulate the formatted row.
s
        Returns:
        - The formatted row string.
        """

        for column, line in enumerate(lineInfo):
            if column == 0:
                toAppendReturn = toAppendReturn + f'{line:^5}' 
                continue
            elif column > 1 and column < 8:
                toAppendReturn = toAppendReturn + f'{line:>10}'
                continue
            toAppendReturn = toAppendReturn + f'{line:>10}' 
        return toAppendReturn

    def Terminal_Output(self):
        """
        Prints the formatted table for the terminal.
        """

        print(TableOutput.fortmated_Table(self))
        print(f"Instant Ticket Sell: {self.instantTotal}")

   

    