import unittest # Importing the unittest module 
from credentials import Credentials # Importing the credentials class
import random

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials   class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def password(length):
        pw = str()   
        characters = "abcdefghijklmnopqrstuvwxyz0123456789"
        for i in range(length):
             pw = pw + random.choice(characters)
        print(pw)
        return pw 
    password(10)