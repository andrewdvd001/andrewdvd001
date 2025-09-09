class Account:
    bank_name = "ABC Bank"

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.__balance = balance

    @classmethod
    def set_bank_name(cls, name):
        cls.bank_name = name
    
    @staticmethod
    def convert_usd_to_idr(usd_amount):
        return usd_amount * 16000
    
    def show_account(self):
        print(f"Owner: {self.owner}, Balance: {self.__balance}, Bank: {Account.bank_name}")

account1 = Account("Andrew", 100)
account1.set_bank_name("Mandiri Bank")
converted = Account.convert_usd_to_idr(90)
print(f"90 USD = {converted} IDR")
account1.show_account()