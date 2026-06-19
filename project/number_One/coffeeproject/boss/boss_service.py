from boss import config as boss_config
import database
from boss import boss_signup
from boss import boss_signin
from boss import boss_modify
from boss import boss_delete

class Management:
    def __init__(self):
        self.fileName = "bossLogin.json"
        self.bossdict = {}

        self.bossdict = database.load_data(self.fileName, self.bossdict)

    def sign_up(self):
        boss_signup.signUp(self.bossdict)
        database.save_data(self.fileName, self.bossdict)
    def sign_in(self):
        boss_signin.bossSignIn(self.bossdict)
    def modifyinfo(self):
        boss_modify.modify(self.bossdict)
        database.save_data(self.fileName, self.bossdict)
    def deleteinfo(self):
        boss_delete.delete(self.bossdict)
        database.save_data(self.fileName, self.bossdict)
   
    def run(self):

        flag = True

        while flag:
            try:
                selectedNum = int(input('1. Sign-Up 2. Sign-In  3. Modify 4. Delete 0. back to main'))  
            except ValueError:
                print('숫자만 입력해주세요.')
                continue

            if  selectedNum == boss_config.SIGN_UP:
                self.sign_up() 
            elif  selectedNum == boss_config.SIGN_IN:
                self.sign_in()  
            elif  selectedNum == boss_config.MODIFY:
                self.modifyinfo()    
            elif  selectedNum == boss_config.DELETE:
                self.deleteinfo() 
            elif  selectedNum == boss_config.BACKTOMAIN:
                flag = False 

if __name__ == "__main__":
    Management().run()