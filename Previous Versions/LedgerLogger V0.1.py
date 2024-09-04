from datetime import date
import json
def setup():
    try:
        item = open("item.json", "r")
        item.close()
    except:
        print("No record found")
        print("Initializing")
        item = open("item.json", "w")
        inivalue = str(input("Enter initial balance: "))
        item.write("{\"initial\":\""+inivalue+"\""+"\n}")
        item.close()
        print("Done")
def log_now():
    global itemindex
    itemstr = str(input("Enter item name:\n"))
    amt = str(input("Input amount: "))
    #type = str(input("Type (Normal/Debit/Credit): "))
    with open(f"item.json", 'r') as file:
        data = json.load(file)
    datenow = str(date.today())
    print(datenow)
    key_to_check = datenow
    try:
        index = list(data.keys()).index(key_to_check)
        data[itemstr] = amt
    except:
        data[datenow] = '0'
        data[itemstr] = amt
    with open("item.json", 'w') as file:
        json.dump(data, file)
    print("Logged")
def check_balance():
    sum = float(0)
    with open(f"item.json", 'r') as file:
        data = json.load(file)
    for key in data:
        value = float(data[key])
        sum += value
    print("Book balance now: " + str(sum))
def export():
    with open(f"item.json", 'r') as file:
        data = json.load(file)
    txt = open("data.txt", "w")
    datatuple = list(data.items())
    for tup in datatuple:
        txt.write(str(tup) + '\n')
    print("Exported as data.txt")
setup()
while True:
    try:
        response = int(input('''
Choose action:
1. Log now (Today's date)
2. Check Balance
3. Export as txt
'''))
    except:
        print("Invalid input")
        continue
    if response == 1:
        log_now()
        continue
    elif response == 2:
        check_balance()
    elif response == 3:
        export()
