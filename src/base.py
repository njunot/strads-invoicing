#!/usr/bin/ python3

'''
Base class of invoicing program. Other data classes will inherit attributes from this class.
'''

class base:
    def add(self):
        pass

    def edit(self, var, val):
        return setattr(self, var, val) 

    def remove(self):
        pass

    def save(self):                         #Database Interfaced
        pass

    def displayAttribute(self):             #Database Interfaced
        pass

    def checkCoupleID(self):                #Database Interfaced
        pass

    def export2csv(self):
        pass


'''
Class dedicated for registering and viewing people
'''
class peopleChart(base):
    adress = None
    company = None
    phone = None
    invoiveIDs = []                         #Generated contents: [InvoiceID, ...]
    communicationIDs = []                   #Generated contents: [CommunicationID, ...]
    
    def __init__(self, name, forename, email):
        self.name = name
        self.forename = forename
        self.email = email
    
    def listOpenInvoices(self):
        # Search term: InvoiceNumber + Status(1)
        pass

    def listAllInvoices(self):
        pass

    def listCommunications(self):
        pass

    def listConversation(self):
        # Depends on variable conversationID
        pass

    def export2vCard(self):
        pass

'''
Class dedicated for invoices
'''
class invoiceChart(base):
    companyBankAccountNumber = None             #Check
    externRef = None                            #Check
    change = None
    amountConverted = None                      #Generated
    date = None                                 #Generated
    sentFlag = False
    paymentReceived = False
    status = 0                                  #Generated
    invoiceNumber = None                        #Generated

    def __init__(self, amount, currency, table):
        self.amount = amount
        self.currency = currency
        self.table = table                      #Content: [category, description, timeSpent, amountCharged]

    def makeInvoices(self):
        pass

    def send(self):
        pass

    def checkBooks(self):
        pass

    def export2GNUCash(self):
        pass

    def export2MT940(self):
        pass


'''
Class dedicated for communications with customers
'''
class communicationChart(base):
    conversationID = None
    flag = []
    archived = False
    communicationID = None
    
    def __init__(self, date, subject, category, coupledPeopleID):
        self.date = date
        self.subject = subject
        self.category = category
        self.coupledPeopleID = coupledPeopleID

    def fetchMail(self):
        pass

    def archive(self):
        pass

    def CheckMail(self):
        pass

    def setFlag(self):
        pass 
