
def check_password(password):
    if len(password) < 9:
        return False
        print ("password must be minimum 9 characters")
    if len(password) > 16:
        return False
        print ("password must be maximum 16 characters")
    if not name.isalpha():
        return False
        print ("password does not contain letters")
    if not name.isnum()):
        return False
        print ("password does not contain numbers")
    return True

