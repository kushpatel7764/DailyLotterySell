"""
    TableOutput class provides methods to handle different types of outputs (terminal, text, Excel) for 
    filtered meteorite data.

    Attributes:
    - outputTypeChosen (str): Represents the user's choice for the type of output.
    - sortedList (list): the sorted list of meteorite objects.
"""

import xlwt
import UtilityFunctions
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
        
        for price in range(7):
            #For each price create a label
            self.price = dict_of_Prices[price]
            tableString = tableString + TableOutput.Create_Terminal_Row_Label(self.price) + "\n"
            tableString = tableString + TableOutput.Draw_Terminal_Table_Sepration_Line(50) + "\n"
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

    def Create_Terminal_Row_Label(price):
        """
        Creates the label row for the terminal table.

        Returns:
        - A formatted string of row labels.
        """

        labels = [f"${price}" ,"OPEN", "CLOSE", "SELL"]
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
        lineInfo = [str(self.row_Number), self.open[price][lineNum], self.close[price][lineNum], self.sell[price][lineNum]] #+1 is added to convert from index to number
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
                toAppendReturn = toAppendReturn + f'{line:^10}' 
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

    def Exel_Output(self):
        """
        Generates an Excel file containing the sorted data. 
        """

        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('Meteor Data')

        TableOutput.Excel_Write_Label(sheet)
        TableOutput.Excel_Write_Data(self, sheet)

        # Save the workbook to a file
        fileName = Useful_Module.get_clean_datetime_string() + ".xls"
        workbook.save(fileName)
        print(f"\nExcel file \"{fileName}\" created successfully.\n")

    def Excel_Write_Label(sheet):
        """
        Writes labels to the Excel sheet.

        Parameters:
        - sheet: An Excel sheet object.
        """

        labels = ["name", "id", "nametype", "recclass", "mass", "fall", "year", "reclat", "reclong", "Geolocation", "States", "Counties"]
        for col, label in enumerate(labels):
            sheet.write(0, col, label)
    
    def Excel_Write_Data(self, sheet):
        """
        Writes data to the Excel sheet. The first loop picks a row and the second loop sets a columbs at a row from the first loop. 

        Parameters:
        - sheet: An Excel sheet object.
        """        

        for row, meteor in enumerate(self.sortedList, start=1):
            data = [meteor.name, meteor.id, meteor.nametype, meteor.recclass, meteor.mass, meteor.fall,
                    meteor.year, meteor.reclat, meteor.reclong, meteor.GeoLocation, meteor.States, meteor.Counties]
            for col, value in enumerate(data):
                sheet.write(row, col, value)

    def Text_Output(self):
        """
        Generates a text file containing the sorted data. The new text file will have the same format as the original 
        meteoroid file. The name of file is determined by get_clean_datetime_string(). 
        """

        fileName = Useful_Module.get_clean_datetime_string() + ".txt"
        textFileOutput = open(fileName, "w")
        textFileOutput.write(TableOutput.TextFile_Table(self))
        print(f"\nText file \"{fileName}\" created successfully.\n")
    
    def TextFile_Table(self, tableString = ""):
        """
        Formats the data for a text file. First a label row is created and then a data row is created. 

        Parameters:
        - tableString (str): A string to accumulate the formatted data.

        Returns:
        - The formatted data string for a text file.
        """

        tableString = tableString + TableOutput.Create_TextFile_Row_Label() + "\n"
        for meteor in self.sortedList:
            tableString = tableString + TableOutput.Create_TextFile_Data_Row(meteor) + "\n"
        return tableString

    def Create_TextFile_Row_Label():
        """
        Creates the row labels for the text file.

        Returns:
        - A formatted string of row labels for a text file.
        """

        labels = ["name", "id", "nametype", "recclass", "mass", "fall", "year", "reclat", "reclong", "Geolocation", "States", "Counties"]
        return TableOutput.setup_TextFile_Row(labels)
        
    def Create_TextFile_Data_Row(sortedObj):
        """
        Creates a data row for the text file using setup_TextFile_Row, it loops through all the meteoroid object attributes in the line and create a row.

        Parameters:
        - sortedObj: An object containing data to be displayed.

        Returns:
        - A formatted string of data for a single row in a text file.
        """

        toReturn = ""
        lineInfo = [sortedObj.name, sortedObj.id, sortedObj.nametype, sortedObj.recclass, sortedObj.mass, sortedObj.fall,
                    sortedObj.year, sortedObj.reclat, sortedObj.reclong, sortedObj.GeoLocation, sortedObj.States, sortedObj.Counties]
        toReturn = TableOutput.setup_TextFile_Row(lineInfo, toReturn)
        return toReturn
    
    def setup_TextFile_Row(lineInfo, toAppendReturn = ""):
        """
        Sets up a row for the text file. It loops through all the meteoroid object attributes (given in lineInfo) and creates a row string. 

        Parameters:
        - lineInfo (list): List of data to be displayed in a row.
        - toAppendReturn (str): A string to accumulate the formatted row.

        Returns:
        - The formatted row string for a text file.
        """

        for column, line in enumerate(lineInfo):
            if column == 11:
                toAppendReturn = toAppendReturn + line
                continue
            toAppendReturn = toAppendReturn + line + "\t" 
        return toAppendReturn


   

    