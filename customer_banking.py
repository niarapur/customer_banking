# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    sav_bal =input(f" Please enter your current savings balance: ")
    savings_balance= float(sav_bal)
    sav_int=input(f" Please enter your current savings interest rate in decimals e.g. for 1% enter 0.01: ")
    savings_interest= float(sav_int)
    sav_mat = input(" Please enter the number of months the account held a balance: ")
    savings_maturity= int(sav_mat)
    # Call the create_savings_account function and pass the variables from the user.
    updated_sav_balance, savings_int_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    updated_savings_balance = '{:,.2f}'.format(updated_sav_balance)
    savings_interest_earned = '{:,.2f}'.format(savings_int_earned)
    print(f"Your current savings interest earned is: $",savings_interest_earned)
    print(f"Based on the above interest earned,your current new savings balance is: $",updated_savings_balance)
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE$
    cd_bal = input(f" Please enter your current CD balance: ")
    cd_balance = float(cd_bal)
    cd_int=input(f" Please enter your current CD interest rate in decimals e.g. for 1% enter 0.01: ")
    cd_interest = float(cd_int)
    cd_mat = input(" Please enter the number of months the CD account held a balance: ")
    cd_maturity= int(cd_mat)
    # Call the create_cd_account function and pass the variables from the user.
    upd_cd_balance, cd_int_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    updated_cd_balance = '{:,.2f}'.format(upd_cd_balance)
    cd_interest_earned = '{:,.2f}'.format(cd_int_earned)
    print(f"Your current CD interest earned is: $",cd_interest_earned)
    print(f"Based on the above interest earned,your new CD balance is: $" ,updated_cd_balance)

if __name__ == "__main__":
    # Call the main function.
    main()
