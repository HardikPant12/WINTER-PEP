
#ATM SIMULATOR
"""
pin = "1234"
balance = 5000

def balance_check():
    print("Current Balance:", balance)

def withdraw_money():
    global balance
    amt = int(input("Enter amount to withdraw: "))
    if amt <= 0:
        print("Invalid amount")
    elif amt <= balance:
        balance -= amt
        print("Please collect your cash")
    else:
        print("Insufficient balance")

def deposit_money():
    global balance
    amt = int(input("Enter amount to deposit: "))
    if amt <= 0:
        print("Invalid amount")
    else:
        balance += amt
        print("Amount deposited successfully")

def pin_change():
    global pin
    old = input("Enter old PIN: ")
    if old == pin:
        pin = input("Enter new PIN: ")
        print("PIN changed successfully")
    else:
        print("Wrong PIN")

while True:
    print("\n--------- ATM MENU ---------")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Change PIN")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        balance_check()
    elif choice == "2":
        withdraw_money()
    elif choice == "3":
        deposit_money()
    elif choice == "4":
        pin_change()
    elif choice == "5":
        print("Thank you for using ATM")
        break
    else:
        print("Invalid choice")
"""

#QUIZ GAME WITH HIGH SCORE
"""
def load_high_score():
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read())
    except:
        return 0

def save_high_score(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))

def play_quiz():
    questions = [
        "Capital of India? ",
        "2 + 2 = ",
        "Python is a ______ language? ",
        "PM of India? "
    ]

    answers = [
        "delhi",
        "4",
        "programming",
        "modi"
    ]

    score = 0

    for i in range(len(questions)):
        user_ans = input(questions[i]).lower()
        if user_ans == answers[i]:
            print("Correct!")
            score += 10
        else:
            print("Wrong!")

    return score

def main():
    high_score = load_high_score()
    name = input("Enter player name: ")

    print("\nWelcome", name)
    print("Previous High Score:", high_score)

    score = play_quiz()

    print("Your Score:", score)

    if score > high_score:
        print("🎉 New High Score!")
        save_high_score(score)
    else:
        print("High Score remains:", high_score)

main()

"""

# EXPENSE CALCULATOR
"""
total_expense = 0

def add_expense(amount):
    global total_expense
    total_expense += amount
    print("Expense added successfully")

def view_expense():
    print("Total Expense:", total_expense)

while True:
    print("\n------ Expense Tracker ------")
    print("1. Add Expense")
    print("2. View Total Expense")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        amt = int(input("Enter expense amount: "))
        add_expense(amt)
    elif choice == "2":
        view_expense()
    elif choice == "3":
        print("Exiting Expense Tracker")
        break
    else:
        print("Invalid choice")


"""