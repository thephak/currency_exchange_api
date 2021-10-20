def to_int(
    input: str
):
    """
    Convert string to integer with error handling
    :param input: String that contains integer number
    :return: Interger number or 0 if the the string is not contains integer number 
    """
    
    try: 
        return int(input)
    except ValueError:
        return 0

def to_float(
    input: str
):
    """
    Convert string to floating point number with error handling
    :param input: String that contains floating point number
    :return: Interger number or 0 if the the string is not contains floating point number
    """
    
    try: 
        return float(input)
    except ValueError:
        return 0
