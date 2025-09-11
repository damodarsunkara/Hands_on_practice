import json
import hashlib

class Customers:
    def __init__(self,name,password):
        self.name=name
        
        self.password = hashlib.sha256(str(password).encode()).hexdigest()
        self.balance=0.0
    def display(self):
        print(f" your current balance is RS {self.balance}")
    def deposit(self,amount):
        if amount>100:
            self.balance+=amount
            
            print(f'u deposited the {amount} is and updated balance is {self.balance}')
           

        else:
            print("invalid amount,must be the greater than 100")
    def withdraw(self,amount):
        if 0<amount<=self.balance:
            self.balance-=amount
            print(f"you withdraw {amount} updated balance :RS {self.balance}")
            
        else:
            print("insufficient balance")
class BankAtm:
    def __init__(self):
        self.customers={}
        self.next_acc=1001
        self.load_data()
        
        
    def save_data(self):
        with open("customers.json","w") as file:
            json.dump(self.customers,file)
    def load_data(self):
        try:
            with open("customers.json","r") as file:
                data =file.read().strip()

                self.customers=json.loads(data) if data else {}
                    

                self.next_acc=max(map(int,self.customers.keys()), default=1001) +1
        except FileNotFoundError:
            print("ACCOUNT NOT FOUND")
            self.customers={}
                
    def create_account(self,name,password):
        acc_no=str(self.next_acc)
        customer =Customers(name,password)
        self.customers[acc_no] ={"name":name, "password":customer.password, "balance": customer.balance}
        self.next_acc+=1
        self.save_data()
        print(f"Account created successfully ! Your account number is:{acc_no}")
        return acc_no
     
    def login(self,acc_no,password):
        
       customer=self.customers.get(acc_no)
       hashed_password =hashlib.sha256(password.encode()).hexdigest()
        
       if customer and customer["password"] == hashed_password:
           print("Login successful !")
           return Customers(customer["name"],password,customer["balance"])
       print("Invalid credentials.")
       return None
    def update_balance(self,acc_no, new_balance):
        self.customers[acc_no]["balance"]=new_balance
        self.save_data()

def main():
    atm=BankAtm()
    while True:
        print("\nwelcome to the small atm bank")
        print("Available services: \n1.CREATE ACCOUNT \n2.LOGIN \n3.EXIT")
        try:
           choice=int(input("ENTER U R CHOICE (1/2/3):\n"))
        except ValueError:
               print("Invalid input.please enter a number")
        
        if choice == 1:
            name=input("ENTER U R NAME:\n").upper()
            while True:
               password=input("SET YOUR PASSOWRD:\n")
               if password.isdigit() and len(password)<=4:
                   break
               else:
                   print("Invalid password.Must be exactly 4 digits.")
            acc_no=atm.create_account(name,password)
       
            
            if input("Do you want to continue with login ?(yes/no) ").lower()=="yes":
               acc_no=input("Enter the account number:")
               password=input("Enter the password")
               user=atm.login(acc_no,password)
               
           
               if user:
                   while True:
                        print("THE SERVICES ARE\n 1.DISPLAY BALANCE \n 2.DEPOSIT AMOUNT \n 3.WITHDRAW AMOUNT \n 4.LOGOUT")
                        service=int(input(" ENTER THE CHOICE WITH NUMBER:\n"))
                        if service== 1:
                             user.display()
                        elif service==2:
                            user_amt=float(input("ENTER THE AMOUNT"))
                            user.deposit(user_amt)
                            atm.udate_balance(acc_no, user.balance)
                        elif service==3:
                                
                            user_amt=int(input("ENTER THE AMOUNT"))

                            user.withdraw(user_amt)
                            atm.update_balance(acc_no, user.balance)
                        elif service==4:
                            print("Logging out")
                            break
                        else:
                            print("INVALID CREDENTIALS")
                    
             
            
        elif choice==2:
            
                acc_no=str(input("ENTER THE ACCOUNT NUMBER:"))
                password=input("ENTER THE PASSWORD ")
                user=atm.login(acc_no,password)
                if user:
                    while True:
                    
                        print("THE SERVICES ARE 1.DISPLAY BALANCE \n 2.DEPOSIT AMOUNT \n 3.WITHDRAW AMOUNT \n 4.logout")
                        service=int(input(" ENTER THE CHOICE WITH NUMBER:\n"))
                        if service == 1:
                              user.display()
                        elif service==2:
                            user_amt=float(input("ENTER THE AMOUNT"))
                            user.deposit(user_amt)
                            atm.update_balance(acc_no, user.balance)
                        elif service==3:
                            
                            user_amt=float(input("ENTER THE AMOUNT"))
                            user.withdraw(user_amt)
                            atm.update_balance(acc_no, user.balance)
                        elif service==4:
                            print("logging out")
                            break
                        else:
                            print("invalid choice")
                    
                    
        elif choice==3:
             print("THANK YOU VISIT AGAIN")
             break
        else:
            print("invalid choice")
                


if __name__=="__main__":
    main()
                    
                

