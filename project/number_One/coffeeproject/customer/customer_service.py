from customer import config as customer_config
import database
from customer import customer_signup
from customer import customer_modify
from customer import customer_delete
from customer import customer_signin

class customerService:
    def __init__(self):
        self.fileName = "customer.json"
        self.customerdict = {}

        self.customerdict = database.load_data(self.fileName, self.customerdict)

    def sign_up(self):
        customer_signup.signUp(self.customerdict)
        database.save_data(self.fileName, self.customerdict)
    def sign_in(self):
        customer_signin.sign_in(self.customerdict)
    def modifyinfo(self):
        customer_modify.modify(self.customerdict)
        database.save_data(self.fileName, self.customerdict)
    def deleteinfo(self):
        customer_delete.delete(self.customerdict)
        database.save_data(self.fileName, self.customerdict)
   
    def run(self):

        flag = True

        while flag:
                
            try:    
                selectedNum = int(input('1. Sign-Up 2. Sign-In  3. Modify 4. Delete 0. back to main   '  ))  
            except ValueError:
                print('숫자만 입력해주세요.')
                continue

            if  selectedNum == customer_config.SIGN_UP:
                self.sign_up() 
            elif  selectedNum == customer_config.INFOCHECK:
                self.sign_in()  
            elif  selectedNum == customer_config.MODIFY:
                self.modifyinfo()    
            elif  selectedNum == customer_config.DELETE:
                self.deleteinfo() 
            elif  selectedNum == customer_config.BACKTOMAIN:
                flag = False 

if __name__ == "__main__":
    customerService().run()