
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

    def __init__(self, filepath):
        Account.__init__(self, filepath)  # this creates a minimal object that inherits from the Account class
                                            # you need to pass the same parameters in the parent and child lasses (it seeems)

checking=Checking("balance.txt")
checking.deposit(10)
print(checking.balance)


# remember CMD + / for multi-line comments

# my_account = Account("balance.txt") # for 'self,' Python will automatically pass the object instance. my_account is the object instance.
# print(my_account.balance)   # uses dot notation to point to the object ("account") that holds the balance attribute 
# my_account.withdraw(100)  # the object instance is passed automatically, but we have to supply the amount.
# print(my_account.balance)  
# my_account.commit() # don't need to pass any argument
