
class Account:

    def __init__(self, filepath):
        with open(filepath,'r') as file: 
            self.balance=int(file.read())  
            # this will save the value of the int from the text file in the instance variable self.balance.
            # you'll need to cast the file.read as an int (it's otherwise a string).

    account = Account("balance.txt") # for 'self,' Python will automatically pass the object instance.