def is_leap_year(year):
    """
    Takes a Year as input and check if it's a leap year or not.
    """
    if year % 4 == 0:
        if year % 100 == 0: #Not a leap year unless divisible by 400
            if year % 400 == 0:
                return True
            else:
                return False      
        else:
            return True
           
    else:
        return False #NOT LEAP


print(is_leap_year(2020))
