""" 
Here we assume that we have a client coming to us asking for an automated Rental Property Calculator. 
Our client's name is Brandon from a company called "Bigger Pockets". 
Below, you will find a video of what Brandon usually does to calculate his Rental Property ROI.
Using Visual Studio Code/Jupyter Notebook, and Object Oriented Programming create a program that will 
calculate the Return on Investment(ROI) for a rental property.
This project will be completed individually, though you can feel free to share ideas with your fellow students.
Once completed, commit the project to github and submit the link to this assignment.
Also come up with a catch phrase for yourself!
"""

# ROI calculator (four square method)
# 1.Income (total of..)
#     - rental income
#     - laundry
#     - storage
#     - parking    
#     - misc
# 2.Expenses (minus these)
#     - taxes
#     - insurance
#     - utilities
#         - electric
#         - water
#         - sewer
#         - garbage
#         - gas
#     - hoa(optional)
#     - lawn care/snow removal
#     - vacancy 5% of rental income
#     - repairs $100 (tenant damage)
#     - CapEx $100 (fundamental repairs, replacements roofs, water heater)
#     - property management 10% of rental income
#     - mortgage
# 3.Cash Flow(difference of)
#     income - expenses
# 4.Cash on Cash ROI
#     - total investment (sum of 4 below)
#         - down payment 20% purchase price
#         - closing costs est: $3,000
#         - rehab budget est. $7,000
#         - misc/other $0
#     - annual cashflow = 12 * cash flow
#     - annual cashflow / total investment = percentage
#         - compare this number to other investments you can make! 


class ROI_Calculator():
    
    def __init__(self):
        self.cashflow = 0
        self.finalIncome = {}
        self.income_num = 0
        self.finalExpenses = {}
        self.expenses_num = 0
        
    def Income(self):
        print("\nPlease enter the income you will recieve from this property. ")
        print("This can include money made from any of the following: ")
        print("rental income, coin laundry, parking space rental, storage rental, furniture rental.")
        print(f"Current income(s) : {self.finalIncome}")
        income_type = input("Enter income type: ")
        income_amount = float(input(f"How much will you make from {income_type} monthly? "))
        self.finalIncome[income_type] = income_amount
        self.cashflow += income_amount
        self.income_num += income_amount
        print(f"Current income(s) : {self.finalIncome}")
        add_more = input("\nWould you like to add another source of income? (y/n) : ")
        if add_more.lower() == "y":
            self.Income() 
        elif add_more.lower() == "n":
            pass
        else:
            print("\nInvalid input, please make a valid selection! ")

    def Expenses(self):
        print("\nPlease enter the expenses you will have from this property. ")
        print("This can include money spent on any of the following: ")
        print("mortgage, vacancy, property management, taxes, insurance, utilities (electric, water, sewer, gas, garbage), HOA fees, lawn care, snow removal,repairs, savings. ")
        print(f"Current exspense(s) : {self.finalExpenses}")
        expense_type = input("Enter the expense type: ")
        expense_amount = float(input(f"How much will {expense_type} cost you monthly? "))
        self.finalExpenses[expense_type] = expense_amount
        self.cashflow -= expense_amount
        self.expenses_num += expense_amount
        print(f"Current expense(s) : {self.finalExpenses}")
        add_more_more = input("\nWould you like to add another expense? (y/n) : ")
        if add_more_more.lower() == "y":
            self.Expenses() 
        elif add_more_more.lower() == "n":
            pass
        else:
            print("\nInvalid input, please make a valid selection! ")

    def CashFlow(self):
        print("\nBased on the following entries:")
        print(f"{self.finalIncome}")
        print(f"Your total income is: ${self.income_num}.") 
        print("\nBased on the following entries:")
        print(f"{self.finalExpenses}")
        print(f"Your expenses are totaling: ${self.expenses_num}.")
        print(f"\nYour cash flow is: ${self.cashflow} !")

    def cashOncashROI(self):
        total_investment = 0
        print("\nThis calculation will give you a percentage that you can check againt other available investment opportunites. ")
        print("Use YOUR best judgement & decide if the property is the right choice for YOU and YOUR plan! ")
        purchase_price = float(input(f"What was the purchase price of the property? "))
        down_payment = (purchase_price * .20)
        total_investment += down_payment
        closing_costs = float(input(f"What amount did you pay in closing costs? If none, enter '0'. "))
        total_investment += closing_costs
        rehab_cost = float(input(f"How much did you spend rehabbing the property? If none, enter '0'. "))
        total_investment += rehab_cost 
        other_spending = float(input(f"If any other amount of money was spent relative to the purchase of this property please enter it here. If none, enter '0'. "))
        total_investment += other_spending
        annual_cashflow = (12 * self.cashflow)
        coc_perc = ((annual_cashflow / total_investment) * 100)
        print(f"\nYour cash on cash ROI is approximately {coc_perc} % !")
        print("Happy investing! ")

class Main():
    def showInstructions():
        print("""
The Deluxe ROI Calculator
Choose from the following:
[1] Add a source of Income
[2] Add an Expense
[3] Figure out your cash flow
[4] Calculate your ROI!
[5] Quit
        """)
    def run():
        Main.showInstructions()
        self = ROI_Calculator()
        while True:
            choice = input("\nWhat would you like to do? ")
            if choice == "1":
                self.Income()
            elif choice == "2":
                self.Expenses()    
            elif choice == "3":
                self.CashFlow()
            elif choice == "4":
                self.cashOncashROI()
            elif choice == "5":
                print("Thanks for using our calculator, Happy Investing! ")
            else:
                print("Invalid input, please make a valid selection! ")
Main.run()