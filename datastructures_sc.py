import re
from icecream import ic

# An Exception class for any type of invalid input
class InvalidInputError(Exception):
    pass
# A class that had validation methods of various kinds, pretty handy for validating input on every method call
class ValidationUtils:
    #This method validates that the input provided is a string and that it matches a regex. Since it uses regex the use cases are very broad. It has special handling for None values. 
    @staticmethod
    def validate_string(value, regex, error_message):
        if value is None:
            return None
        if isinstance(value, str) and re.match(regex, value):
            return value
        else:
            raise InvalidInputError(error_message)
    #This methods simply validates that the input provided is a positive integer or float. It has special handling for None values. 
    @staticmethod
    def validate_positive_number(value, error_message):
        if value is None:
            return None
        if isinstance(value, (int, float)) and value > 0:
            return value
        else:
            raise InvalidInputError(error_message)

class CreditCard:
    # Validates and adds attributes to the istance of the class. If some attribute is not provided during the creation of the class the value of the attribute defaults to None. This is to not stop the creation of an incomplete classes, since set methods are defined for this class. 
    def __init__(self, customer=None, bank=None, account=None, limit=None):
        self._customer = ValidationUtils.validate_string(customer, r'^[a-zA-Z_\s]+$', 'Customer must be a string and can only have English alphabet letters, whitespaces, and underscores')
        self._bank = ValidationUtils.validate_string(bank, r'^[a-zA-Z_\s]+$', 'Bank must be a string and can only have English alphabet letters, whitespaces, and underscores')
        self._account = ValidationUtils.validate_string(account, r'^\s*(\d{4} *){4}\s*$', 'Account must be a string consisting of 16 numbers, ideally separated by a space every 4 numbers. E.g., 1234 5678 9101 1121')
        self._limit = ValidationUtils.validate_positive_number(limit, 'Limit must be a positive float or integer')
        self._balance = 0
    # Customer getter, setter and deleter methods. It runs a string validation for the setter. 
    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, new_customer):
        self._customer = ValidationUtils.validate_string(new_customer, r'^[a-zA-Z_\s]+$', 'Customer must be a string and can only have English alphabet letters, whitespaces, and underscores')
    
    @customer.deleter
    def customer(self):
        self._customer = None
    # Bank getter, setter and deleter methods. It runs a string validation for the setter. 
    @property
    def bank(self):
        return self._bank

    @bank.setter
    def bank(self, new_bank):
        self._bank = ValidationUtils.validate_string(new_bank, r'^[a-zA-Z_\s]+$', 'Bank must be a string and can only have English alphabet letters, whitespaces, and underscores')

    @bank.deleter
    def bank(self):
        self._bank = None
    # Account getter, setter and deleter methods. It runs a string validation for the setter. 
    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, new_account):
        self._account = ValidationUtils.validate_string(new_account, r'^\s*(\d{4} *){4}\s*$', 'Account must be a string consisting of 16 numbers, ideally separated by a space every 4 numbers. E.g., 1234 5678 9101 1121')

    @account.deleter
    def account(self):
        self._account = None
    # Account getter, setter and deleter methods. It runs a positive integer validation for the setter.
    @property
    def limit(self):
        return self._limit

    @limit.setter
    def limit(self, new_limit):
        self._limit = ValidationUtils.validate_positive_number(new_limit, 'Limit must be a positive float or integer')
    
    @limit.deleter
    def limit(self):
        self._limit = None
    # Charge method. It charges to the card if the charge doesn't exceed the limit and if it is a positive integer or float. 
    def charge(self, price):
        validated_price = ValidationUtils.validate_positive_number(price, 'Invalid price provided. Price must be a positive float or integer')
        if validated_price + self._balance <= self._limit:
            self._balance += validated_price
            return True
        else: 
            return False
    # Payment method. It pays to the credit card if the payment is a positive integer or a float. It returns a string with the amount of change in case a payment greater than the balance is provided.     
    def make_payment(self, payment):
        validated_payment = ValidationUtils.validate_positive_number(payment, 'Invalid payment provided. Payment must be a positive float or integer')
        if self._balance - validated_payment >= 0:
            self._balance -= validated_payment
            return True
        else: 
            change = abs(self._balance - validated_payment)
            self._balance = 0
            return f'Your change is {change}'

myCard = CreditCard('a', 'a', '1234123412341234', 1000)
myCard.charge(500)
ic(myCard._balance)
ic(myCard.make_payment(600))
ic(myCard._balance)