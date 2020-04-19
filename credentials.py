class Credentials:
    """
    class that generates new instances of credentials
    """

    credentials_list=[] # Empty user list

    def __init__(self,first_name,last_name,email,):


        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    # import random
    # def password(length):
    #     pw = str()   
    #     characters = "abcdef"
    #     for i in range(length):
    #          pw = pw + random.choice(characters)
    #     print(pw)
    #     return pw 
    # password(10)
 