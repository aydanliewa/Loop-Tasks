#Python loops tasks



#Part A-Easy



#Rocket launch
for i in range (10,0,-1):
    print(i)
print("Liftoff!")



#Cinema tickets
child_count=0
adult_count=0
for i in range(1,6):
    visitor_age=int(input())
    if visitor_age < 18:
        child_count=child_count+1
    else:
        adult_count=adult_count+1
print("Child tickets:", child_count)
print("Adult tickets:", adult_count)



#Read the code

#It prints 
#1 3 5 7 9


for i in range(1,10,2):
    print(i,end=" ")



#Shopping basket
total=0
for i in range (1, 6):
    price_of_item=float(input())
    total=total+price_of_item
average=total/5
print("Total:", total)
print("Average:", average)



#Choose a password
password=""
while len(password)<8:
    password=input("New password: ")
    if len(password)<8:
        print("Too short, try again")
print("Password accepted")



#Read the code
#70
#40
#10
#-20
#Done

balance=100
while balance>0:
    balance= balance-30
    print(balance)
print("Done")



#Step counter
total=0
daily_step=1200
for i in range(1,8):
    total=total+daily_step
    print("Day", i, ":", total)



#Simple login

for attempt in range(1,4):
    username=input("Username: ")
    password=input("Password: ")
    if username=="admin" and password=="1234":
        print("Welcome!")
        break
    else:
        if attempt<3:
            print("Wrong username or password")
        else:
            print("Account locked")
        





#Part-B Medium



#ATM Withdrawal
balance=500
while True:
    amount=float(input())
    if amount==0:
        print("Goodbye")
        break
    elif amount<0:
        print("Invalid amount")
    elif amount>balance:
        print("Insufficient funds")
    else:
        balance=balance-amount
        print("Balance:", balance)



#Read the code


#Wrong PIN, 2 attempts left
#Wrong PIN, 1 attempts left
#Access granted
#Attempts used: 3


pin="1234"
attempts=0
while attempts<3:
    entered=input("PIN: ")
    attempts=attempts+1
    if entered==pin:
        print("Access granted")
        break
    print("Wrong PIN,", 3-attempts, "attempts left")
print("Attempts used:", attempts)



#Exam results
passed=0
failed=0
highest=0
totalgrades=0
count=0
while True:
    grade=int(input())
    if grade==-1:
        break
    if grade>=51:
        passed=passed+1
    else:
        failed=failed+1
    if grade > highest or count == 0:
        highest=grade
    totalgrades=totalgrades+grade
    count=count+1
average=totalgrades/count
average=round(average,1)
print("Passed:", passed)
print("Failed:", failed)
print("Highest:", highest)
print("Average:", average)



#Parking garage
free_spaces=20
while True:
    command=input()
    if command=="stop":
        break
    elif command=="in":
        if free_spaces<=0:
            print("Garage full")
        else:
            free_spaces=free_spaces-1
            print("Free spaces:", free_spaces)
    elif command=="out":
        if free_spaces>=20:
            print("Garage is empty")
        else:
            free_spaces=free_spaces+1
            print("Free spaces:", free_spaces)
    else:
        print("Unknown command")



#Weather report
count=0
hottest_temperature=0
hottest_day=0
for day in range(1,8):
    temperature=int(input())
    if temperature>30:
        count=count+1
        if temperature > hottest_temperature or hottest_day == 0 :
            hottest_temperature=temperature
            hottest_day=day
print("Hot days:", count)
print("Hottest day:", hottest_day)


            
#Find the bug
#The bug is the place of attempts=0. It was placed inside the loop,so it reset on every step causing an infinite loop.
#Fixed Code
password="secret"
attempts=0
while True:
    entered=input("Password: ")
    if entered==password:
        print("Welcome")
        break
    attempts=attempts+1
    if attempts==3:
        print("Account locked")
        break



#Password stength

password=input()
digits=0
uppercase=0
lowercase=0
for i in password:
    if i.isdigit():
        digits+=1
    elif i.isupper():
        uppercase+=1
    elif i.islower():
        lowercase+=1
if len(password)<8:
    print("Weak password: not enough characters")
if digits==0:
    print("Weak password:no digits")
if uppercase==0:
    print("Weak password:no uppercase letters")
if lowercase==0:
    print("Weak password: no lowercase letters")
else:
    print("Strong password")




#Savings goal


month=0
savings=0
monthly_savings=50
while savings<1000:
    savings=savings+monthly_savings
    month=month+1
    print("Month: ", month, savings)
    monthly_savings=monthly_savings+10
print("Goal reached in month ", month)



#Read the code
#It prints 105, because 105 is divisible by 7 and it is an odd  number.
#Break stops while loop as soon as the first number is found.
number=100
while True:
    number=number+1
    if number%7==0 and number%2==1:
        break
print(number)



#Part C- Hard



#Bank account menu

pin="2580"
balance=1000
attempts=0
while attempts<3:
    enteredpin=input("Enter PIN: ")
    if enteredpin==pin:
        break
    else:
        attempts+=1
if attempts==3:
    print("Card blocked")
else:
    while True:
        print("1-Check balance")
        print("2-Deposit")
        print("3-Withdraw")
        print("4-Exit")
        option=int(input("Choose an option: "))
        if option==1:
            print("Balance: ", balance, "AZN")
        elif option==2:
            deposit=float(input())
            if deposit<=0:
                print("Invalid amount")
            else:
                balance=balance+deposit
                print("New balance: ", balance, "AZN")
        elif option==3:
            withdraw=float(input())
            if withdraw<0 or withdraw>balance:
                print("Invalid or insufficient amount")
            else:
                balance=balance-withdraw
                print("New balance: ", balance, "AZN")
        elif option==4:
            print("Goodbye")
            break
        else:
            print("Invalid choice")



#Vending machine

total=0.0
accepted_coins=[0.05,0.10,0.20,0.50,1.0]
while total<1.50:
    insert_coin=float(input())
    if accepted_coins.count(insert_coin)==1:
        total=total+insert_coin
        print("Total: ", round(total,2 ))
    else:
        print("Coin not accepted")
change=total-1.50
change=round(change,2)
print("Here is your water")
print("Change: ", change)



#Door codes

count=0
for i in range(2,101):
    k=0
    for j in range(1,i+1):
        if i%j==0:
            k=k+1
    if k==2:
        count=count+1
        print(i,end=" ")
print("Total codes: ", count)



#Read the code
#It prints:
#101 102
#201 202
#301 302


for floor in range(1,4):
    for room in range(1,5):
        if room==3:
            break
        print(floor*100+room, end=" ")
    print()



#Hotel room list

for floor in range(1,6):
    if floor==4:
        break
    for room in range(1,5):
        print("Floor", floor,":",floor*100+room, end=" ")
    print()



#Bank queue

totaltime=480
customers=0
while totaltime>0:
    customertime=int(input())
    if customertime==0:
        break
    if customertime>totaltime:
        print("Sorry, come back tomorrow")
        break
    totaltime=totaltime-customertime
    customers+=1
print("Customers served: ", customers)
print("Minutes left: ", totaltime)



#Vote counting


votes_for_a=0
votes_for_b=0
votes_for_c=0
spoiledvotes=0
while True:
    vote=input()
    if vote=="end":
        break
    if vote=="A":
        votes_for_a+=1
    elif vote=="B":
        votes_for_b+=1
    elif vote=="C":
        votes_for_c+=1
    else:
        spoiledvotes+=1
    print("A: ",votes_for_a, "B: ", votes_for_b, "C: ", votes_for_a)
    print("Spoiled votes: ", spoiledvotes)
    maxvote=max(votes_for_a, votes_for_b, votes_for_c)
    if votes_for_a==maxvote and votes_for_b==maxvote:
        print("Winner: Tie")
    elif votes_for_a==maxvote and votes_for_c==maxvote:
         print("Winner: Tie")
    elif votes_for_b==maxvote and votes_for_c==maxvote:
         print("Winner: Tie")
    elif votes_for_a==maxvote:
        print("Winner: A")
    elif votes_for_b==maxvote:
        print("Winner: B")
    else:
        print("Winner: C")



#Card number check



while True:
    card=input()
    if len(card)!=16 or not card.isdigit():
        print("Must be 16 digits")
        continue
    sum=0
    for i in range(15,-1,-1):
        card_number=int(card[i])
        if (15-i)%2==1:
            card_number=card_number*2
            if card_number>9:
                card_number=card_number-9
        sum=sum+card_number
    if sum%10==0:
        print("Valid card number")
    else:
        print("Invalid card number")
    break
