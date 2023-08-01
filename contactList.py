# main program
def start():
    contactList = createTestContacts()
    print("Nu visar vi kontaktlistan vid start")
    showContactList(contactList)
    print("------------------------------------------")

    while True:
        choose = input("n = new contact\nl = show list\nq = quit\n->").lower()
        print(choose)
        if choose == "n":
            createOneContact(contactList)
        elif choose == "l":
            showContactList(contactList)
        elif choose == "q":
            endOfContactlist()
            exit()
    
   

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
    #Updaterar listan
    contactList.append([contactName,contactAge,contactNumber])
    return contactList

def showContactList(contactList):
    print("Nu visar vi kontaktlistan")
    # print(contactList)

    for contact in contactList:
        print(contact)

 



def endOfContactlist():
    print("Slut i rutan")


start()
