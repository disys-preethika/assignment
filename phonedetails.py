import datetime

class phonecontacts:

    def __init__ (self,uname,kname,num1,num2,email,dofb):
        self.conname=uname
        self.nickname=kname
        self.phonenumber1=num1
        self.phonenumber2=num2
        self.emailid=email
        self.inputDate=dofb
        

    def contact(self):
        print("------phone_contacts details-----")
        print("""
              1.contactname
              2.nick_name
              3.phonenumber_1
              4.phonenumber_2
              5.email_id
              6.birth_date
              """)
        
    def contactname(self):
        conname=input("Enter the contact name:")
        print("contact is:"+conname)
        if type(self.conname)==str:
            if len(self.conname)<= 20:                                                                                
                print("name verified")
        else:
            raise TypeError("The name should not contain numbers and symbols")

    def nick_name(self):
        nickname=input("Enter the nick name:")
        print("nickname is:"+nickname)
        if type(self.nickname)==str:
            if len(self.nickname)<= 20:                                                                                
                print("name verified")
        else:
            raise TypeError("The name should not contain numbers and symbols")
    

    def phonenumber_1(self):
        phonenumber1=input("Enter the phone number:")
        print("The Phone number is:"+phonenumber1)
        if (len(phonenumber1)==10):
            if type(phonenumber1)==int:
                print("phone-number 1 verified")
        else:
            raise ValueError("The phone-number should not letters and symbols")

        

    def phonenumber_2(self):

       phonenumber2=input("Enter the phone number:")
       print("The Phone number is:"+phonenumber2)
       if (len(phonenumber2)==10):
           if type(phonenumber2)==int:                                                                            
                print("phone-number 2 verified")
       else:
           raise ValueError("The phone-number should not contain letters and symbols")
    

    def email_id(self):
        emailid=input("Enter the email id:")
        print("The email id is:"+emailid)
        if type(emailid)==str:
            if len(emailid)<= 30:  
                print("email_id is verified")
        else:
            raise TypeError("Invalid email-id")

    def BirthDate(self):
        self.inputDate = input("Enter the date of birth : ")
        day,month,year = inputDate.split('/')
        isValidDate = True
        try :
            datetime.datetime(int(year),int(month),int(day))
        except ValueError :
            isValidDate = False
        if(isValidDate):
            print ("Valid date of birth")
        else:
            print ("Invalid birthdate")

    def __del__(self):
        del self.conname
        del self.nickname
        del self.phonenumber1
        del self.phonenumber2
        del self.emailid
        del self.inputDate
        
        

    

phone=phonecontacts("preethika","preethi",7708592085,7010201775,"preethi001",22/11/22)
phone.contact()
phone.contactname()
phone.nick_name()
phone.phonenumber_1()
phone.phonenumber_2()
phone.email_id()
phone.BirthDate()




       
