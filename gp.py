class pay:                                                                                  
    
    def __init__(self,Email_ID,Phone_number,Name,Account_number):                                                                 
        self.emailid=Email_ID
        self.mobile=Phone_number
        self.username=Name
        self.Account=Account_number
        
    def open_gpay(self):
        
        print("Welcome to pay")
        
        
    def email_authentication(self):
         emailid=input("Enter the email id:")
         print("The email id is:"+emailid)
         if type(emailid) == str:
            if len(emailid)<= 15:                                                                              
                print("email_id is verified")
            else:
                raise ValueError("The Email-id should not contain more than 30 values")
         else:
            raise TypeError("Invalid email-id")
    def mobile_authentication(self):
        mobile=input("Enter the phone number:")
        print("The Phone number is:"+mobile)
                  
        if (len(mobile)==10) :
            if (type(mobile) == int):                                                                            
                print("phone-number verified")
        else:
            raise TypeError("The phone-number should contain only integers ")
                
    def name_authentication(self):
        username=input("Enter the username:")
        print("username is:"+username)
        if type(username)==str:
            if len(username)<= 20:                                                                                #LEN FUNCTION
                print("name verified")
            else:
                raise ValueError("The name should contain only lesser than or equal to 20 letters")
        else:
            raise TypeError("The name should contain letters only")

    def otp_authentication(self,code,otp):
        if(otp==code):
            print("Otp is verified")
        else:
            raise ValueError("The OTP you are entered is not correct")

    def Bank_authentication(self):
        Account=input("Enter your account number:")
        print("Account number is:"+Account)
        if type(Account)==str:
            if(len(Account)==10):
                 print("Bank account Verified")
            else:
                raise TypeError("The number should be equal to 10")
        else:
            raise TypeError("This is a invalid bank account number")
           
           
       

    def Pin_generation(self,number):
        self.pin=number
        if (len(self.pin)==4):
            print("your pin is successfully created")
        else:
            raise ValueError("Invalid pin_number")

    def Pin_updation(self,match,Pin):
        self.match=match
        self.pinno=Pin
        if self.match==self.pinno:
            print("user pin is matched")
            print("Transaction successful")
        else:
            raise ValueError("pin not matched")
            print("Transaction failed")

        





