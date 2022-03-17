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
new = ""
while new.lower() != "stop" and action.lower() != "stop":
    cls()
    new = input("What would you like to do?\n   Login   Create   Delete\n")
    while new.lower() != "create" and new.lower() != "login" and new.lower() != "delete":
        cls()
        new = input("What would you like to do?\n   Login   Create   Delete\n")
    #if you want to create
    if new.lower() == "create":
        cls()
        naming = input("What is the name of the account?\n")
        cls()
        passwording = input("What is the password of the account?\n")
        if os.path.exists(f"{naming}_____.csv"):
            cls()
            print("This account already exists.")
            time.sleep(2)
            cont = 0
        else:
            file = open("accounts.csv", "a")
            file.writelines(f"{naming},{passwording}\n")
            cont = 1
            file = open(f"{naming}_____.csv", "a")
            cls()
            file.writelines("Budget,Amount,Spent,Left\n")
            input(f"Welcome to the budgeting system of {naming}. Press enter to continue into the program.\n")
            cls()
    #if you want to login
    if new.lower() == "login":
        attempting = attempts
        cls()
        account = input("What account do you want to access?\n")
        cls()
        passwords = input("What is the password?\n")
        if os.path.exists(f"{account}_____.csv"):
            recreate = (f"{account}/_____/.csv")
            recreate.split("/")
            with open(f'accounts.csv', 'r') as read_obj:
                csv_reader = reader(read_obj)
                for row in csv_reader:
                    if row[0] == account:
                        password = str(row[1])
                    else:
                        continue
            if password == passwords:
                input(f"Welcome to the budgeting system of {account}. Press enter to continue into the program.\n")
                cont = 1
            else:
                cont = 0
        else:
            input("Sorry, but that account does not exist. Press enter to continue.\n")
            cont = 0
    if new.lower() == "delete":
        contactinfo = []
        cls()
        account = input("What account do you want to delete?\n")
        cls()
        passwords = input("What is the password of the account you want to delete?\n")
        file = f"{account}_____.csv"
        if(os.path.exists(file) and os.path.isfile(file)):
            os.remove(file)
            cls()
            with open('accounts.csv', 'r') as file:
                file = reader(file)
                for row in file:
                    if row[0] == account:
                        continue
                    else:
                        contactinfo.append(row)
            with open('accounts.csv', 'w') as file:
                file.writelines(contactinfo)
        cont = 0

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
    while cont == 1:
        while action.lower() != "stop" and cont == 1:
            creation = []
            cls()
            action = input("What would you like to do?\n1. Add Budget\n2. Delete Budget\n3. Look at Budget\n4. Edit Budget\n")
            budget = []
            if action.lower() == "add budget" or action.lower() == "add" or action.isnumeric() == 1:
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
            elif action.lower() == "delete budget" or action.lower() == "delete" or action.isnumeric() == 2:
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
            elif action.lower() == "look at budget" or action.lower() == "look at" or action.isnumeric() == 3:
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
            elif action.lower() == "edit budget" or action.lower() == "edit" or action.isnumeric() == 4:
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
            elif action.lower() == "leave":
                cont = 0
password = ""
cls()
