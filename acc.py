
class Account:

    def __init__(self, filepath):
        self.class_filepath = filepath  # this makes filepath available anywhere in the class (notice the giveaway name)
        with open(filepath,'r') as file: 
            self.balance=int(file.read())  
            # this will save the value of the int from the text file in the instance variable self.balance.
            # you'll need to cast the file.read as an int (it's otherwise a string).

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):  # both 'amount' variables are local, so they can have the same name. 
        self.balance = self.balance + amount

    def commit(self):
        with open(self.class_filepath, 'w') as file:  # we open the filepath (see above) into to overwrite ('w') text file with updates. 
            file.write(str(self.balance))

class Checking(Account): # need to pass the base class in as an argument

    # an example of a doc string, which you can pull out with print(object.__doc__).
    # They're very useful when you're importing classes from modules
    """This class generates checking accoujnt objects"""

    type="checking" # a class variable is declared outside the methods contained by that class
                    # they are shared by all instances of that class

    def __init__(self, filepath, fee):      # conventionally thought of as a "constructor"
        Account.__init__(self, filepath)    # this creates a minimal object that inherits from the Account class
                                            # you need to pass the same parameters in the parent and child lasses (it seeems)
        self.fee = fee                      # Transform this fee into an instance variable

    def transfer(self, amount, fee):
        self.balance = self.balance - amount - self.fee

# these two below are both "instantiation":
jack_checking=Checking("jack.txt", 2) # it seems self is automatically passed as the instance is created
jack_checking.transfer(20,2)
print(jack_checking.balance)  # prints out the balance instance variable of the base Class
jack_checking.commit()        # commits the change of the operation to balance.txt

# separate instance
john_checking=Checking("john.txt", 2) # it seems self is automatically passed as the instance is created
john_checking.transfer(10,2)
print(john_checking.balance)  # prints out the balance instance variable of the base Class
john_checking.commit() 

# remember CMD + / for multi-line comments

# my_account = Account("balance.txt") # for 'self,' Python will automatically pass the object instance. my_account is the object instance.
# print(my_account.balance)   # uses dot notation to point to the object ("account") that holds the balance attribute 
# my_account.withdraw(100)  # the object instance is passed automatically, but we have to supply the amount.
# print(my_account.balance)  
# my_account.commit() # don't need to pass any argument
