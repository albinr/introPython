
# main program
def start():
    contactList = []
    while True:
        choose = input().lower()
        if choose == "new":
            createOneContact(contactList)
        elif choose == "contacts":
            showContactList(contactList)
    contactList = createTestContacts(contactList)
    createOneContact(contactList)
    showContactList(contactList)
    endOfContactlist()
    




# defenitions of functions

def createTestContacts(contactList):
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

    ShowOneContact(contactList)


def ShowOneContact(contactList):
    print("-- Nu visar vi en kontakt")

def endOfContactlist():
    print("Slut i rutan")



start()