class CreditCard:
    """Consumer Creadit Card"""
    
    def __init__(self,customer,bank,account,limit):
        self._customer=customer
        self._bank=bank
        self._account=account
        self._limit=limit
        self._balance=0
    
    def get_customer(self):
        '''output :Customer Name'''
        return self._customer
    
    def set_name(self):
        ''' set or change: Name of customers'''

    def charge(self,charge_amount):
        if charge_amount+self._balance >  self._limit:
            return False
        else:
            self._balance+=charge_amount
            return True
    
    def make_payment(self,amount):
            if amount<=0:
                return False
                print(self._balance)
            else:
                self._balance-=amount
                print(self._balance)
                return True
    
    def get_details(self):
        print('ythe name is '+str(self._customer)+"the amount is "+str(self._balance))


if __name__=="__main__":
    credcard=CreditCard("KULDEEP",'bankop',"dssad",2000)
    credcard.get_details()
    if credcard.charge(1000):
        credcard.get_details()
    else:
        credcard.get_details()
    if credcard.make_payment(300):
        credcard.get_details()
    else:
        credcard.get_details()
