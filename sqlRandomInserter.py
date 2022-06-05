import mysql.connector as sql
import random

names = open("names.txt","r")
addresses = open("addresses.txt","r")


mydb = sql.connect(
    host = "localhost",
    user = "root",
    password = "*****",         #password is based on what you set it as in mysql
    database = "myDatabase"
)


cursor = mydb.cursor()

insertCommand = """INSERT INTO customers(name,address) VALUES(%s,%s)"""

def putRecord(name,address):
    cursor.execute("INSERT INTO customers(name,address) VALUES(%s,%s)", (name,address) )
    mydb.commit()
    print(name + " " + address + " INSERTED")



def putRandomRecords(amount):
    records = []
    nameList = names.read().split("\n")
    addressList = addresses.read().split("\n")
    for i in range(amount):
        name = ""
        address = ""
        while not name:
            name = nameList[random.randint(0,len(nameList)-1)]
        while not address:
            address = addressList[random.randint(0,len(addressList)-1)]
        records.append((name,address))
        print(i)
    cursor.executemany(insertCommand,records)
    mydb.commit()
    


def main():
    num = input("Type how many new random records to insert: ")
    putRandomRecords(int(num))
    input("\nPress enter to close")



if __name__ == "__main__":
    main()

    
