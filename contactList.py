# main program
def start():
    # contactList = createTestContacts()
    contactList = readContactsFromFile()
    print("Nu visar vi kontaktlistan vid start")
    showContactList(contactList)
    print("------------------------------------------")

    while True:
        choose = input("n = new contact\nl = show list\nq = quit\n-> ").lower()
        print(choose)
        if choose == "n":
            createOneContact(contactList)
        elif choose == "l":
            showContactList(contactList)
        elif choose == "q":
            endOfContactList()
            exit()
        else:
            print("invalid option! Try again!")
    
   

# defenitions of functions

def createTestContacts():
    print("Här ligger test contacter")
    contactList = [["Albin", 23, "0707"], ["Jonas", 58, "0705"]]
    print(contactList)
    return contactList

def createOneContact(contactList):
    print("Input: Här matar vi in en contact och lägger in sist i contact list")
    contactName = input("Name: ")
    contactAge = input("Age: ")
    contactNumber = input("Number: ")

    # Update the list and the file
    contactList.append([contactName, contactAge, contactNumber])
    with open('contacts.txt', 'a') as file:
        file.write(",".join([contactName, contactAge, contactNumber]) + "\n")
    return contactList

def readContactsFromFile():
    try:
        with open('contacts.txt', 'r') as file:
            lines = file.readlines()
            contactList = [line.strip().split(",") for line in lines]
            return contactList
    except FileNotFoundError:
        return []

def showContactList(contactList):
    print("Nu visar vi kontaktlistan")
    # print(contactList)

    for contact in contactList:
        print(contact)

 



def endOfContactList():
    print("Slut i rutan")


start()
