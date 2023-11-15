"""
ATM SIMULATION PROJECT
"""
"""
THE USER PIN IS 00001
THE ACCOUNT NUMBER IS 0123456789
THE DEFAULT ACCOUNT BALANCE IS 50000
"""
  #WELCOME MESSAGE
print('*'*30)
print('WELCOME DEAR VALUED CUSTOMER')
print('*'*30)
print('ENTER YOUR ACCOUNT NUMBER AND PIN BELOW TO PROCEED TO THE TRANSACTION INTERFACE')

  #ALREADY STORED USER DATA
user_name = 'THOMAS SHELBY'
stored_pin = int('00001')
stored_account_number = int('0123456789')
user_account_balance = int('50000')
withdrawal_menu = {1:1000, 2:2000, 3:5000, 4:10000, 5:20000, 6:0}

  #PROMPT FOR USER PIN AND ACCOUNT NUMBER
user_pin = int(input('ENTER YOUR PIN: '))
account_number = int(input('ENTER YOUR ACCOUNT NUMBER: '))

  #ACCOUNT NUMBER AND USER PIN VERIFICATION
if user_pin == stored_pin and account_number == stored_account_number:
  
  while True:
      #TO DISPLAY MAIN MENU AND SUB-MENUS
    print('Main menu:' + '\n\t 1 - View my balance' + '\n\t 2 - Withdraw cash' + '\n\t 3 - Deposit Funds' + '\n\t 4 - Exit')
    user_choice = int(input('ENTER A CHOICE: '))
    
      #TO DISPLAY ACCOUNT BALANCE
    if user_choice == 1:
      print(f'YOUR ACCOUNT BALANCE IS {user_account_balance}')
      
      #TO DISPLAY WITHDRAWAL MENU
    elif user_choice == 2:
      print('Withdrawal menu:' + '\n\t 1 - 1000' + '\t 2 - 2000' + '\n\t 3 - 5000' + '\t 4 - 10000' + '\n\t 5 - 20000' + '\t 6 - Cancel Transaction.')
      withdrawal_choice = int(input('CHOOSE A WITHDRAWAL AMOUNT: '))
      withdrawal_amount = withdrawal_menu[withdrawal_choice]
      
      #TO UPDATE USER ACCOUNT BALANCE AFTER WITHDRAWAL
      for num,amount in withdrawal_menu.items():
        if withdrawal_choice == num and withdrawal_choice != 6:
          user_account_balance = user_account_balance - amount
          print('WITHDRAWAL SUCCESSFUL')
          print(f'{amount} HAS BEEN DEDUCTED FROM YOUR ACCOUNT')
          print(f'YOUR CURRENT BALANCE IS: {user_account_balance}')
          
      #TO TERMINATE WITHDRAWAL PROCESS
      if withdrawal_choice == 6:
        print('WITHDRAWAL TERMINATED')
      if withdrawal_amount > user_account_balance:
        second_withdrawal_choice = int(input('CHOOSE ANOTHER AMOUNT: '))
        withdrawal_amount = withdrawal_menu[second_withdrawal_choice]
        user_account_balance = user_account_balance - withdrawal_amount
        print('YOUR BALANCE NOW IS' + str(user_account_balance ))
        
      #TO ENABLE USER DEPOSIT FUNDS
    elif user_choice == 3:
      deposit_amount = int(input('ENTER YOUR DEPOSIT AMOUNT OR TYPE "0" TO CANCEL: '))
      
      #TO TERMINATE DEPOSIT PROCESS
      if deposit_amount == int(0):
        quit
        
      #TO UPDATE USER ACCOUNT BALANCE AFTER DEPOSIT 
      else:
        user_account_balance = deposit_amount + user_account_balance
        print(f'{deposit_amount} HAS SUCCESSFULLY BEEN DEPOSITED TO ACCOUNT')
        print(f'YOUR NEW ACCOUNT BALANCE IS {user_account_balance}')
        
      #TO EXIT MAIN MENU
    elif user_choice == 4:
      break
    
      #IF USER LOGIN VERIFICATION FAILS
else: 
  i = 0
  while i <= 1:
    print('WRONG INPUT ---- PLEASE RE-ENTER YOUR DETAILS: ')
    user_pin_prompt = int(input('ENTER YOUR PIN: '))
    account_number_prompt = int(input('ENTER YOUR ACCOUNT NUMBER: '))
    i +=1 
