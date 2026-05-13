
balance=0
while True:
    print("1 for Deposit, 2 for withdraw, 3 for check balance, 4 to exit")
    choice= int(input("enter you choice "))
    if(choice == 1):
        amount=int(input("enter the amount you want to deposit "))
        balance+=amount
    elif(choice ==2):
        amount=int(input("enter the amount to withdraw "))
        if(amount>balance):
            print("insufficient balance")
        else:
            balance-=amount
            print("withdraw successful ")
    elif(choice == 3):
        print("your current balance is ",balance)
    elif(choice == 4):
        print("thank you for using our services")
        break
    else:
        print("invalid choice, please try again")   
    



    