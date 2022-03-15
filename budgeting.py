import os, csv, webbrowser, time, random
from sqlite3 import Row
from attemptings import attemptings
import pandas as pd
from csv import DictWriter, reader
def cls():
    os.system('cls')
cls()
action = ""
videos = ['https://www.youtube.com/watch?v=CVCuN_q1K_g', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'https://www.youtube.com/watch?v=OQj4bQEu-xA', 'https://www.youtube.com/watch?v=vm112M4ToLM', 'https://www.youtube.com/watch?v=cvh0nX08nRw', 'https://www.youtube.com/watch?v=jDwVkXVHIqg', 'https://www.youtube.com/watch?v=wrdK57qgNqA', 'https://www.youtube.com/watch?v=gM4S9lPyUUA', 'https://www.youtube.com/watch?v=8zEQeHcKMXM', 'https://www.youtube.com/watch?v=NW-qSGZByH8']
cls()
attempts = 3
#Login or Create
new = input("What would you like to do?\n   Login      Create\n")
while new.lower() != "stop" and action.lower() != "stop":
    while new.lower() != "create" and new.lower() != "login":
        cls()
        new = input("What would you like to do?\n   Login      Create\n")
    #if you want to create
    if new.lower() == "create":
        cls()
        naming = input("What is the name of the account?\n")
        cls()
        passwording = input("What is the password of the account?\n")
        if os.path.exists(f"{naming}{passwording}.csv"):
            cls()
            print("This account already exists.")
            time.sleep(2)
        else:
            accounts = open("accounts.csv", "a")
            accounts.writelines(f"{naming},{passwording}")
        file = open(f"{naming}{passwording}.csv", "a")
        cls()
        input(f"Welcome to the budgeting system of {naming}. Press enter to continue into the program.\n")
        cls()
    #if you want to login
    if new.lower() == "login":
        attempting = attempts
        account = input("What account do you want to access?\n")
        cls()
        passwords = input("What is the password?\n")
        cls()
        if os.path.exists(f"{account}{passwords}.csv"):
            recreate = (f"{account}/{passwords}/.csv")
            recreate.split("/")
            while recreate[1] != passwords:
                attempts = 2
                while attempts != 0:
                    if recreate[1] != passwords:
                        attempts -= 1
                        passwords = input("Sorry, that is incorrect.\nWhat is the password?\n")
                    else:
                        break
                    cls()
                cls()
                if attempts == 0:
                    attemptings(attempting, time, cls)
            if recreate[1] == passwords:
                input(f"Welcome to the budgeting system of {account}. Press enter to continue into the program.\n")
            file = open(f"{account}{passwords}.csv", "a")
        else:
            input("Sorry, but that account does not exist. Press enter to continue.\n")
    df = pd.read_csv(file)
    if df.empty == True:
        file.writelines("Budget,Amount,Spent,Left")

    def budgetfunc(budget):
        cls()
        budget = []
        with open(f'{naming}{passwording}.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            for row in csv_reader:
                if row[0] != "Budget":
                    budget.append(row[0])
        print(budget)
    def creating(looking, adding, creation):
        with open(f'{naming}{passwording}.csv', 'r') as read_obj:
            csv_reader = reader(read_obj)
            for row in csv_reader:
                if row[0] == looking:
                    budgets = row[0]
                    if action.lower() == "spent":
                        amount = int(row[1])
                        spent = adding
                    elif action.lower() == "amount":
                        amount = adding
                        spent = int(row[2])
                    left = amount - spent
                    adds = [budgets, amount, spent, left]
                    creation.append(adds)
                if row[0] != looking:
                    creation.append(row)
        with open(f'{naming}{passwording}.csv', "w", newline="") as b:
            writer = csv.writer(b)
            writer.writerows(creation)
    while action.lower() != "stop":
        creation = []
        cls()
        action = input("What would you like to do?\n Add Budget   Delete Budget   Look at Budget   Edit Budget\n")
        budget = []
        if action.lower() == "add budget" or action.lower() == "add":
            cls()
            budgetadd = input("What budget would you like to add?\n")
            cls()
            budgetamount = int(input("What is the budgeting amount?\n"))
            cls()
            budgetspent = int(input("How much have you spent so far?\n"))
            cls()
            budgetleft = budgetamount - budgetspent
            budgetingadd = [budgetadd, budgetamount, budgetspent, budgetleft]
            with open(f'{naming}{passwording}.csv', 'a', newline="") as f:
                writer = csv.writer(f)
                writer.writerow(budgetingadd)
        elif action.lower() == "delete budget" or action.lower() == "delete":
            budgetfunc(budget)
            budgetdelete = input("What budget would you like to delete?\n")
            cls()
            with open(f'{naming}{passwording}.csv', 'r') as read_obj:
                csv_reader = reader(read_obj)
                for row in csv_reader:
                    if row[0].lower() != budgetdelete.lower():
                        budget.append(row)
            with open(f'{naming}{passwording}.csv', "w", newline="") as b:
                writer = csv.writer(b)
                writer.writerows(budget)
        elif action.lower() == "look at budget" or action.lower() == "look at":
            budgetfunc(budget)
            looking = input("What budget would you like to look at?\n")
            with open(f'{naming}{passwording}.csv', 'r') as read_obj:
                csv_reader = reader(read_obj)
                for row in csv_reader:
                    if row[0].lower() == looking.lower():
                        budgets = row[0]
                        amount = row[1]
                        spent = row[2]
                        left = row[3]
                        cls()
                        #prints budget info
                        input(f"Budget: {budgets}\nAmount: {amount}\nSpent: {spent}\nLeft: {left}\nPress Enter to continue.\n")
        #action is editing
        elif action.lower() == "edit budget" or action.lower() == "edit":
            budgetfunc(budget)
            #asks for what budget you want to edit
            looking = input("What budget would you like to edit?\n")
            creation = []
            cls()
            #editing total amount or total spent
            action = input("What would you like to edit?\n   Amount   Spent\n")
            if action.lower() == "amount":
                cls()
                #asks for new budget amount
                adding = int(input("What is the new budget amount?\n"))
                creating(looking, adding, creation)
            elif action.lower() == "spent":
                cls()
                #asks for new amount spent
                adding = int(input("What is the new amount spent?\n"))
                creating(looking, adding, creation)
        elif action.lower() == "other stuff":
            while True:
                webbrowser.open(random.choice(videos))
                time.sleep(5)
password = ""
cls()