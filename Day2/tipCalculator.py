print("Welcome to the tip calculator!")
bill = float(input("What amount was your bill? $")) 
percent = int(input("What percent would you like to tip? "))
n = int(input("How many people are splittingg this bill? "))

tip = (percent/100) * bill
bill_w_tip = bill + tip
individual_bill = bill_w_tip / n

print(f"Each person needs to pay: ${round(individual_bill, 2)}")
