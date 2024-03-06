import math
 
class Financial_Calculator:
    def __init__(self):
        self.user_info = {}
 
    def get_input(self, prompt, data_type):
        while True:
            try:
                user_input = data_type(input(prompt))
                return user_input
            except ValueError:
                print("Error: Please enter the required info in the input field: ")
 
    def save_user_info(self):
        with open("user_info.txt", "a") as file:
            for key, value in self.user_info.items():
                file.write(f"{key}: {value}\n")
 
    def calculate_investment(self):
        p = self.get_input("How much are you depositing? R", float)
        r = self.get_input("At which interest rate percentile? ", float) / 100 / 12
        t = self.get_input("How many years are you planning to invest for? ", float)
        simp_comp = self.get_input("Choose 'Simple' or 'Compound' interest: ", str).lower()
 
        if simp_comp == "simple":
            total = p * (1 + r * t)
        else:
            total = p * math.pow((1 + r), t)
 
        print(f"Your interest earned over {t} years will be R{total - p:.2f}")
        print(f"Your total amount earned over {t} years will be R{total:.2f}")
       
        self.user_info["Investment"] = f"Principal: {p}, Interest Rate: {r}, Time: {t}, Type: {simp_comp}"
 
    def calculate_bond(self):
        p = self.get_input("What is the current value of the house? R", float)
        i = self.get_input("At which interest rate percentile? ", float) / 100 / 12 / 12
        n = self.get_input("How many months you plan to repay? ", float)
       
        monthly = (i * p) / (1 - (1 + i) ** (-n))
        total_repayment = monthly * n
       
        print(f"Your monthly repayment will be R{monthly:.2f}")
        print(f"Your total repayment will be R{total_repayment:.2f}")
       
        self.user_info["Bond"] = f"Principal: {p}, Interest Rate: {i}, Months: {n}"
 
    def run(self):
        name = input("Please enter your name: ")
        print(f"Hello, {name} mfowethu! Welcome to the A.O.S Financial Calculator.")
 
        while True:
            invest_or_bond = self.get_input(
                '''====================
                Choose either investment or bond from the menu below to proceed:
                  - [ investment ]
                  - [ bond ]
                =====================''',
                str
            ).lower()
 
            if invest_or_bond == "investment":
                self.calculate_investment()
                restart = self.get_input("Do you want to restart the process? (y/n): ", str).lower()
                if restart == "y":
                    continue  
                else:
                    print("Goodbye! Have a great day fam.")
                    break  
            elif invest_or_bond == "bond":
                self.calculate_bond()
                restart = self.get_input("Do you want to restart the process? (y/n): ", str).lower()
                if restart == "y":
                    continue  
                elif restart == "n":
                    print("Goodbye! Have a great day fam.")
                    break  
            else:
                print("Error: Invalid choice. Please choose either 'investment' or 'bond'.")
 
        self.save_user_info()
 
calculator = Financial_Calculator()
calculator.run()