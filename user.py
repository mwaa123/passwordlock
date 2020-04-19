class User:
    """
    class that generates new instances of users
    """

    user_list=[] # Empty user list

    def __init__(self,first_name,last_name,email,password):


 

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def save_user_details(self):
        """
        save_contact method saves user objects into user_list
        """
        User.users_list.append(self)

    @classmethod
    def log_in(cls, name, password):
        '''
        Method that allows a user to log into their credential
        Args:
            name : name of the user
            password : password for the user
        Returns:
            Credential list for the user that matches the name and password
            False: if the name or password is incorrect
        '''

        # Search for the user in the user list
        for user in cls.users_list:
            if user.first_name == name and user.last_name == password:
                return Credential.credential_list

        return False

    @classmethod
    def display_users(cls):
        """
        method that returns the class list
        """
        return cls.users_list

 