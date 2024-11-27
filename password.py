
def check_password(password):
    if len(password) < 9:
        return False
        print ("password is under 9 characters")
    if len(password) > 12:
        return False
        print ("password is above 12 characters")
    if not name.isalpha():
        return False
        print ("password does not contain letters")
    if not name.isnum()):
        return False
        print ("password does not contain numbers")
    return True

