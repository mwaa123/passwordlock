import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

 # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Ruth","Mugo","ruthwanjiramugo@gmail.com","ruthmugo2020") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''


    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        User.users_list = []

    def test_init(self):
        """
        test_init test case to test if object utilizes proper instantiation
        """
        self.assertEqual(self.new_user.first_name,"Ruth")
        self.assertEqual(self.new_user.last_name,"Mugo")
        self.assertEqual(self.new_user.email,"ruthwanjiramugo@gmail.com")
        self.assertEqual(self.new_user.password,"ruthmugo2020")

    def test_save_user(self):
        """
         test case to test if the user object is saved in
         users array
        """
        self.new_user.save_user_details()  # saving the new user
        self.assertEqual(len(User.users_list), 1)

    # def test_save_multiple_users(self):
    #     """
    #         this test-case method gives users the ability to save multiple account details
    #     """
    #     self.new_user.save_user_details()
    #     test_user = User("Test", "user","test@user.com","ruthmugo2020")  # new user
    #     test_user.save_user_details()
    #     self.assertEqual(len(User.users_list), 2)

    def test_log_in(self):
        '''
        Test case to test if a user can log into their credentials
        '''

        # Save the new user
        self.new_user.save_user_details()

        test_user = User("Ruth", "Mugo","ruthwanjiramugo@gmail.com","ruthmugo2020")

        test_user.save_user_details()

        found_credential = User.log_in("Ruth", "Mugo","ruthmugo2020")

        self.assertEqual(found_credential, Credential.credential_list)

    def test_display_all_users(self):
        """
        method that returns a list of all users saved
        """
        self.assertEqual(User.display_users(), User.users_list)
   



if __name__ == '__main__':
    unittest.main()

    