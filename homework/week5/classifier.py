def is_string_int(s):
    '''
    This function takes in the parameter s as a string and returns True
    if s can be safely converted to an int.  It returns False otherwise.
    '''
    try:
        int(s)
    except TypeError:
        return False
    return True


def is_string_float(s):
    '''
    This function takes in the parameter s as a string and returns True
    if s can be safely converted to a float.  It returns False otherwise.
    '''
    try:
        float(s)
    except TypeError:
        return False
    return True


def prompt():
    user_input = raw_input("What string do you want to know about? ")
    if:
        is_string_int(user_input)
        print "%s is an int." % user_input
    elif:
        is_string_float(user_input)
        print "%s is a float." % user_input
    else:
        print "%s does not look like an int, nor a float." % user_input
    
