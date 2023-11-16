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
    def validate_positive_number(value, error_message, types = (int, float)):
        if value is None:
            return None
        if isinstance(value, types) and value >= 0:
            return value
        else:
            raise InvalidInputError(error_message)
    @staticmethod
    def validate_numeric_list(value, error_message) :
        if isinstance(value, list) and all(isinstance(x, (int, float)) for x in value):
            return value
        else: 
            raise InvalidInputError(error_message)
    @staticmethod
    def validate_boolean(value, error_message):
        if isinstance(value, bool):
            return value
        else: 
            raise InvalidInputError(error_message)
        
class CreditCard:
    # Validates and adds attributes to the istance of the class. If some attribute is not provided during the creation of the class the value of the attribute defaults to None. This is to not stop the creation of an incomplete classes, since set methods are defined for this class. 
    def __init__(self, customer=None, bank=None, account=None, limit=None, balance=0):
        self._customer = ValidationUtils.validate_string(customer, r'^[a-zA-Z_\s]+$', 'Customer must be a string and can only have English alphabet letters, whitespaces, and underscores')
        self._bank = ValidationUtils.validate_string(bank, r'^[a-zA-Z_\s]+$', 'Bank must be a string and can only have English alphabet letters, whitespaces, and underscores')
        self._account = ValidationUtils.validate_string(account, r'^\s*(\d{4} *){4}\s*$', 'Account must be a string consisting of 16 numbers, ideally separated by a space every 4 numbers. E.g., 1234 5678 9101 1121')
        self._limit = ValidationUtils.validate_positive_number(limit, 'Limit must be a positive float or integer')
        self._balance = ValidationUtils.validate_positive_number(balance, 'Balance must either be zero or a positive float or integer')
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

    @property
    def balance(self):
        return self._balance
    # Private set and delete balance methods. They should be used by other classes that inherit from CreditCard. 
    def _set_balance(self, new_balance):
        self._balance = ValidationUtils.validate_positive_number(new_balance, 'Balance must either be zero or a positive float or integer')
    
    def _delete_balance(self):
        self._balance = 0
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
            return True, 'Your change:', change

class Vector: 
    # If integer n is provided it assigns to _coords a list of n zeroes. If a list of numeric (int or float) is provided it assigns the list to _coord. Otherwise it raises InvalidInputError
    def __init__(self, value):
        if type(value) == int:
            self._coords = [0] * value
        else:
            self._coords = ValidationUtils.validate_numeric_list(value, f'Value for __init__ must be a list of numeric (int or float) types or an integer. {value} of type {type(value)} was provided')
    # _coords getter, setter and deleter methods. Setter is different to __setitem__ in that it assigns the whole coordinates, not just a value. Deleter assigns every coordinate to 0 instead of actually deleting the attribute
    @property
    def coords(self):
        return self._coords
    @coords.setter
    def coords(self, value):
        self._coords = ValidationUtils.validate_numeric_list(value, f'Coords must be a list of numeric (int or float) types. {value} of type {type(value)} was provided') 
    @coords.deleter
    def coords(self):
        self._coords = [0] * len(self._coords)
    # Adding the supported behaviours for len(Vector), Vector[i], and Vector[i] = value.
    def __len__(self):
        return len(self._coords)
    def __getitem__(self, j):
        return self._coords[j]
    def __setitem__(self, j, value):
        self._coords[j] = value
    # Error handling for inputing an instance of a different type as an other argument.
    def _handle_error(self, other):
        if not isinstance(other, (Vector, list)):
            raise InvalidInputError(f'Addition error between Vector type and {type(other)}. Vector only supports addition between other instances of the Vector class or between a Vector and a numeric list (int or float)')
    # Addition. These methods validate that the other member of the addition is either a vector or an iterable of the same dimension. 
    def _add_vectors(self, other):
        self._handle_error(other)
        if len(self) != len(other):
            raise InvalidInputError(f'Dimensions of vectors must agree. Dimension of first vector is {len(self)} while dimension of second vector is {len(other)}')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __add__(self, other):
        return self._add_vectors(other)
    # __radd__ implementation, so addition works both ways. It's important to clarify that my own implementation only allows for addition of Vector types. I decided this to make the class more Robust.
    def __radd__(self, other):
        return self._add_vectors(other)
    # Multiplication methods (dot product, scalar product). These methods validate that the other member of the multiplication is either an integer or an iterable of the same dimension. 
    def _multiply_vector(self, other):
        result = 0
        if isinstance(other, (int, float)):
            for j in range(len(self)):
                result[j] = self[j] * other
        elif isinstance(other, (Vector, list)) and len(self) == len(other):
            for j in range(len(self)):
                result += self[j] * other[j]     
        else: 
            raise InvalidInputError(f'Provided secondary value "{other}" of type {type(other)} must be an instance of (int, float, vector, list). In case of being vector or list it must be of the same dimension.')
        return result
    def __mul__(self, other):
        return self._multiply_vector(other)
    def __rmul__(self, other):
        return self._multiply_vector(other)    
    # Special substraction method for two Vector types. It validates that both values are vectors and that they're of the same dimension. 
    def __sub__(self, other):
        self._handle_error(other)
        if len(self) != len(other):
            raise InvalidInputError(f'Dimensions of vectors must agree. Dimension of first vector is {len(self)} while dimension of second vector is {len(other)}')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
    # Special handling for __neg__ for the Vector Class. Ir returns the vector with all of the values being -value. 
    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]
        return result
    # Special handling for equality and inequality between Vector types
    def __eq__(self, other):
        self._handle_error(other)
        return self._coords == other._coords
    def __ne__(self, other):
        self._handle_error(other)
        return not self == other
    # Special handling for str(Vector)
    def __str__(self):
        return '<' + str(self.coords)[1:-1] + '>'

class PredatoryCreditCard(CreditCard):
    # Initializes new values that will be needed for the predatory class, including monthly values that are restarted everytime process_month is called. 
    def __init__(self, customer, bank, account, limit, balance, apr, min_payment_percentage, late_fee):
        super().__init__(customer, bank, account, limit, balance)
        self._apr = ValidationUtils.validate_positive_number(apr, f'Apr must be a positive numeric value (int or float)')
        self._min_payment_percentage = ValidationUtils.validate_positive_number(min_payment_percentage, 'Minimum payment percentage must be a positive numeric value (int or float)')
        self._late_fee = ValidationUtils.validate_positive_number(late_fee, 'Late fee must be a positive numeric value (int or float)')
        self._month_calls = 0
        self._month_payment = 0
    # Charges 1 if more than 10 calls have been made in the month. Charges 5 if the charge is unsuccesful. Takes advantage of the parent charge method. 
    def charge(self, price):
        if self._month_calls > 10:
            self._balance += 1
        succes = super().charge(price)
        if not succes:
            self._balance += 5
        return succes
    # Calculates the debt that will be carried out to the next month. Restarts the month counters. Makes the appropiate charges if minimum payment was not met. 
    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor
            min_payment = self._balance * self._min_payment_percentage / 100
            if self._month_payment < min_payment:
                self._balance += self._late_fee
        self._month_calls = 0
        self._month_payment = 0
    # This is merely an extension of the CreditClass make payment that adds a little bit of code that will save the amount of money that was payed during the month. 
    def make_payment(self, payment):
        validated_payment = ValidationUtils.validate_positive_number(payment, 'Invalid payment provided. Payment must be a positive float or integer')
        if self._balance - validated_payment >= 0:
            self._month_payment += validated_payment
            self._balance -= validated_payment
            return True
        else: 
            change = abs(self._balance - validated_payment)
            self._balance = 0
            return True, 'Your change:', change