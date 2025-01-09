'''
**Task: Create an ATM Application**

1. **Features:**
   - The program should provide the following options:
     1. Check Balance  
     2. Withdraw Money  
     3. Deposit Money  
     4. Exit  

2. **Requirements:**
   - Use **if-else** or a **switch-like structure** to handle user input for options.
   - Use a class with the following methods:
     - `check_balance`: Display the current account balance.
     - `withdraw`: Deduct the specified amount from the account balance.
     - `deposit`: Add the specified amount to the account balance.
     - Use a `classmethod` for deposit functionality.

3. **Initial Setup:**
   - Start with an initial account balance of `10000`.

4. **Input:**
   - Accept the user's choice (1, 2, 3, or 4) as a **command-line argument**.

5. **Output:**
   - Display appropriate messages based on the user's choice.
'''

import sys

list=sys.argv

accBal=10000
#print(accBal)

print("Select from below option input number: 1. Check Balance  2. Withdraw Money  3. Deposit Money  4. Exit")
# Using Dictionaries for Switch-Like Behavior
def case_one():
    return "Account Balance is: "+accBal

def case_two():
     withd_amt=int(input("Enter amount you want to withdraw: "))
     print("Withdrawl successesful","----Remaining Balance is: ",accBal=withd_amt)

def case_three():
     depo_amt=int(input("Enter amount you want to deposit: "))
     print("Amount deposited successfully!","---Current Balance: ",accBal+depo_amt)

def case_four():
     exit()

def default_case():
    return "Invalid option."

switch = {
    1: case_one,
    2: case_two,
    3: case_three,
    4: case_four
}

choice = int(input("Enter your choice (1, 2, 3, 4): "))

# Execute the function from the switch dictionary or default
result = switch.get(choice, default_case)()
print(result)

