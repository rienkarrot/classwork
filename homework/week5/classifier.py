def is_string_int(s):
    """
    This function takes in the parameter s as a string and returns True
    if s can be safely converted to an int.  It returns False otherwise.
    """
    try:
        int(s)
    except:
    return
    pass


def is_string_float(s):
    """
    This function takes in the parameter s as a string and returns True
    if s can be safely converted to a float.  It returns False otherwise.
    """
    try:
        float(s)
    except:
    return
    pass

def prompt():
user_input = raw_input("What string do you want to know about? ")
is_string_int(s)
is_string_float(s)
