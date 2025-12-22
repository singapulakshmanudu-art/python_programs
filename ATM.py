balance=1000
def deposit(amount):
    global balance
    balance+=amount   
def withdraw(amount):
    global balance
    if amount<=balance:
        balance-=amount
    else:
        print("Insufficient amount")
deposit(500)
withdraw(400)
print("Balance:", balance)
