class Credentials:
    """
    class that generates new instances of credentials
    """

    credentials_list=[] # Empty user list

    def __init__(self,first_name,last_name,password,):


        self.first_name = first_name
        self.last_name = last_name
        self.password = password


    # def save_credential(self):
    #     """A save_client credentials method"""

    #     Credential.credential_list.append(self)

    # def delete_credential(self):
    #     """This methods, at runtime, with complementary function allows users to delete details"""

    #     Credential.credential_list.remove(self)

    # @classmethod
    # def find_by_first_name(cls, first_name):
    #     """ A user can find details of the account using this method"""
    #     for credential in cls.credential_list:
    #         if credential.first_name == first_name:
    #             return credential

    # @classmethod
    # def credential_exist(cls, password):
    #     """This method allows users to locate existing credentials"""
    #     for credential in cls.credential_list:
    #         if credential.password == password:
    #             return True

    # @classmethod
    # def display_credentials(cls):
    #     """This function allows users to display details saved in their saved accounts """
    #     return cls.credential_list

    # import random
    # def password(length):
    #     pw = str()   
    #     characters = "abcdef"
    #     for i in range(length):
    #          pw = pw + random.choice(characters)
    #     print(pw)
    #     return pw 
    # password(10)
 