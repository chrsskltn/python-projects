# Define a function to calculate tip and total meal cost
def calculate_tip():
    # Ask user for the meal cost and convert to float
    cost = input("What is the cost? ")
    cost = float(cost)

    # Ask user for the tip percentage and convert to float
    tip_percent = input("What is the tip percentage? ")
    tip_percent = float(tip_percent)

    # Calculate the tip and total cost
    tip_amount = cost * (tip_percent / 100)
    total = cost + tip_amount

    # Display the results rounded to 2 decimal places
    print("You should leave a tip of $", round(tip_amount, 2))
    print("The total cost is $", round(total, 2))

# Call the function to run once
calculate_tip()

run_again = input("Do you want to run the program again? Y/N") 
print(run_again)
