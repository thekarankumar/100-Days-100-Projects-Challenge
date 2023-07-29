# Day 2

# Project: Tip Calculator
print("Hello, Welcome To Tip Calculator :)\n")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

split = round(float(((bill+tip)/people)), 2)
print(f"Each person should pay: ${split}")
