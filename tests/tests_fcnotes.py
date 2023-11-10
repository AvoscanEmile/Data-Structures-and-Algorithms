import unittest
import sys
sys.path.insert(0, r'C:\\Users\\avosc\\Documents\\Emile\\Coding\\Python\\notes')
from datastructures_sc import Vector, InvalidInputError, CreditCard

class TestSecondChapter(unittest.TestCase):
    def test_vector_initialization(self):
        # Test initialization with an integer
        vec_int = Vector(5)
        self.assertEqual(len(vec_int), 5)

        # Test initialization with a valid list of integers
        vec_list = Vector([1, 2, 3, 4])
        self.assertEqual(len(vec_list), 4)

        # Test initialization with an invalid list
        with self.assertRaises(InvalidInputError):
            Vector([1, 2, 'invalid'])
            
    def test_vector_operations(self):
        # Create vectors for testing operations
        vec_1 = Vector([1, 2, 3])
        vec_2 = Vector([4, 5, 6])

        # Test addition
        result_addition = vec_1 + vec_2
        self.assertEqual(result_addition.coords, [5, 7, 9])

        # Test invalid addition
        with self.assertRaises(InvalidInputError):
            invalid_result = vec_1 + [4, 5, 6]

        # Test vector equality
        self.assertTrue(vec_1 == Vector([1, 2, 3]))
        self.assertFalse(vec_1 == vec_2)

        # Test vector inequality
        self.assertTrue(vec_1 != vec_2)
        self.assertFalse(vec_1 != Vector([1, 2, 3]))

    def test_vector_modification(self):
        vec = Vector(3)
        # Test setting and getting values
        vec[0] = 10
        self.assertEqual(vec[0], 10)

        # Test modifying the whole coordinates
        vec.coords = [5, 5, 5]
        self.assertEqual(vec.coords, [5, 5, 5])

    def test_vector_deletion(self):
        vec = Vector(4)
        del vec.coords
        self.assertEqual(vec.coords, [0, 0, 0, 0])
    def setUp(self):
        # Creating a sample CreditCard instance for testing
        self.credit_card = CreditCard(customer="John Doe", bank="Bank ABC", account="1234 5678 9101 1121", limit=1000.0)

    def test_customer_property(self):
        self.assertEqual(self.credit_card.customer, "John Doe")

    def test_customer_setter(self):
        self.credit_card.customer = "Jane Doe"
        self.assertEqual(self.credit_card.customer, "Jane Doe")

    def test_customer_setter_invalid_input(self):
        with self.assertRaises(InvalidInputError):
            self.credit_card.customer = 123

    def test_customer_deleter(self):
        del self.credit_card.customer
        self.assertIsNone(self.credit_card.customer)

    def test_bank_property(self):
        self.assertEqual(self.credit_card.bank, "Bank ABC")

    # Add similar tests for bank setter, deleter, and other properties and methods

    def test_charge_valid(self):
        result = self.credit_card.charge(500.0)
        self.assertTrue(result)
        self.assertEqual(self.credit_card._balance, 500.0)

    def test_charge_invalid_price(self):
        with self.assertRaises(InvalidInputError):
            self.credit_card.charge("invalid")
if __name__ == '__main__':
    unittest.main()
