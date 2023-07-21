
# main program
def start():
    contactList = {}
    contactList = createTestContacts(contactList)
    createContact(contactList)
    showContactList(contactList)
    endOfContactlist()



# defenitions of functions

def createTestContacts(contactList):
    print("Här ligger test contacter")
    # contactList = (("Albin", 23, "0707"), ("Jonas", 58, "0705"))
    print(contactList)
    return contactList
    
def createContact(contactList):
    print("Input: Här matar vi in ContaltList")
    InputOneContact(contactList)
    print("Name:")
    contactName = input()
    print("Age:")
    contactAge = input()
    # print("Number:")
    # contactNumber = input()
    contactList.update({contactName:contactAge})

def InputOneContact(contactList):
    print("-- Här matar vi in en enda kontakt")



#  GoGoGo Albin:  Skriv ut i fint, med rubriker

def showContactList(contactList):
    print("Nu visar vi kontaktlistan")
    print(contactList)
    ShowOneContact(contactList)


def ShowOneContact(contactList):
    print("-- Nu visar vi en kontakt")

def endOfContactlist():
    print("Slut i rutan")



start()