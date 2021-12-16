import gp


preethi=gp.pay("preethi0013","9965879085","preethika","3020102010")
preethi.open_gpay()
preethi.email_authentication()
preethi.mobile_authentication()
preethi.name_authentication()
preethi.otp_authentication(15698,15698)
preethi.Bank_authentication()
preethi.Pin_generation("5384")
preethi.Pin_updation(3465,3465)

class Phone_pe(gp.pay):                                                                                                                            
    def __init__(self,Email_ID,Phone_number,Name,Account_number):
        
        super().__init__(Email_ID,Phone_number,Name,Account_number)

    def open_phonepe(self):
        print("Phone pe")
        
amul=Phone_pe("preethika001","9965879086","amulraj","5060406090")
amul.open_phonepe()
amul.email_authentication()
amul.mobile_authentication()
amul.name_authentication()
amul.otp_authentication(780965,780965)
amul.Bank_verification()
amul.Pin_generation("2387")
amul.Pin_updation(3564,3564)


        



