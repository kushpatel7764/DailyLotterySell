def _string_is_numerical(in_string):
        """ 
        returns True if the incoming parameter can be converted to float (i.e. is a number)
        returns False otherwise - checks for TypeError and ValueError on incoming value
        """  

        try:
            float(in_string)
            return True
        except TypeError:
            return False
        except ValueError:
            return False
        
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

def int_arry_to_string_arry(int_arry):
        to_return = []
        for digit in int_arry:
            to_return.append(str(digit))
        return to_return



def user_string_to_array(userInput):
    #strip() - will remove leading and trailing white spaces
    temp_string = userInput.strip()
    temp_array = temp_string.split(" ")
    return temp_array

