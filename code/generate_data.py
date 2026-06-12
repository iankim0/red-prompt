from faker import Faker 
import random 

fake = Faker()

def generate_entry():
    name = fake.name()
    email = fake.free_email()
    accountNumber = fake.swift8()
    routingNumber = fake.bban()
    balance = str(random.randint(0, 999999))
    monthlySpend = str(random.randint(0,10))
    transactions = str(random.randint(0,20))
    entry = name + "," + email + "," + accountNumber + "," + routingNumber + "," + balance + "," + monthlySpend + "," + transactions + "\n"
    return entry

with open("trustedbank.csv", "w") as db:
    db.write("ID,Name,Email,Account Number,Routing Number,Balance,Monthly Spend,Transactions\n")
    db.write("1,Ian Kim,ik7@williams.edu,PMZJGB4W,MYNB48764759382421,0,10,1\n")
    for i in range(49):
        dbEntry = str(i+2) + "," + generate_entry() 
        db.write(dbEntry)
