""" 
This is an Emi_Calculator.
This code calculates the EMI a student will need to pay after taking an education loan. 
This takes care of all the variables like principle amount, repayment and moratorium period, interest rate etc.
"""

p = int(input("Principal: "))
r = float(input("Rate: "))
m = int(input("Moratorium period (in months): "))
t = int(input("Time exclusive of moratorium: "))
family_income = float(input("Family income: "))
r_m = r/1200
S = p*r_m*m
S_amt = S + p

if family_income <= 450000:
    P_eff = p
else:
    P_eff = S_amt

if t <= 0:
    print("Error: Time period must be greater than 0")
    exit()

if r_m == 0:
    EMI = P_eff / t
else:
    denominator = ((1 + r_m)**t) - 1
    if denominator == 0:
        print("Error: Invalid calculation parameters")
        exit()
    EMI = P_eff * r_m * ((1 + r_m)**t) / denominator

print("EMI: ", EMI)
