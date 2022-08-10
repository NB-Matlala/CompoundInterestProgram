import math

print("Welcome to the NB investment portal!")
print("Please input the info required to begin the process\n\n")

age = int(input("How old are you? "))

income = int(input("How much are you paid in ZAR? "))
principal = int(input("How much are you willing to invest(Investments start from ZAR100)?"))

while (principal <100):
    print("\nMinimum investment is 100ZAR.")
    principal = int(input("How much are you willing to invest(Investments start from ZAR100)?"))
else:
    time = int(input('How long do you want to invest(In years)? '))

    print('Interest rate is 16% per annum')
    interestRate = 0.16
finalAmount = principal* 1 + pow(interestRate,time)

print("\n=========================================")
print(f"Investor Age: {age}")
print("Income: " + "R{:,.2f}".format(income))
print(f"Investment duration: {time} years")
print(f"Interest Rate: {interestRate * 100}%")
print("\nNet Profit of Investment: "+"R{:,.2f}".format(finalAmount))
print("=========================================")	
