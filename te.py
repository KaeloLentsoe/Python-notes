import math

class Financial_Calculator:
    def __init__(self):
        self.invest_or_bond = input(
            '''====================
            Choose either investment or bond from the menu below to proceed:
              - [ investment ]
              - [ bond ] 
              ==================='''
        ).lower()
        self.validate_menu_choice()

    def validate_menu_choice(self):
        while self.invest_or_bond not in ["investment", "bond"]:
            print("Please enter a valid choice (investment or bond).")
            self.invest_or_bond = input().lower()

    def get_numeric_input(self, prompt):
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print("Please enter a valid numeric value.")

    def calculate_investment(self):
        p = self.get_numeric_input("How much are you depositing?\nR")
        r = self.get_numeric_input("At which interest rate percentile?\n")
        t = self.get_numeric_input("How many years are you planning to invest for?\n")
        simp_comp = input("Choose 'Simple' or 'Compound' interest.\n").lower()

        if simp_comp == "simple":
            total = p * (1 + r / 100 / 12 * t)
        elif simp_comp == "compound":
            total = p * math.pow((1 + r / 100 / 12), t)
        else:
            print("Please enter a valid choice for interest type (Simple or Compound).")
            return

        print(f"Your interest earned over {t} years will be R{total:.2f}")
        print(f"Your total amount earned over {t} years will be R{total + p:.2f}")

    def calculate_bond(self):
        p = self.get_numeric_input("What is the current value of the house?\nR")
        i = self.get_numeric_input("At which interest rate percentile?\n")
        n = self.get_numeric_input("How many months you plan to repay?\n")
        i = ((i / 100) / 12) / 12

        if n <= 0:
            print("Please enter a valid positive value for the repayment period.")
            return

        monthly = math.floor((i * p) / (1 - math.pow((1 + i), -n)))
        print(f"Your monthly repayment will be R{monthly:.2f}")
        print(f"Your total repayment will be R{monthly * n:.2f}")

    def calculate(self):
        if self.invest_or_bond == "investment":
            self.calculate_investment()
        elif self.invest_or_bond == "bond":
            self.calculate_bond()


# Create an instance of Financial_Calculator
calculator = Financial_Calculator()
calculator.calculate()
