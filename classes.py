class Patient():
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def checkMinor(self):
        if self.age < 21:
            print self.firstname + ' ' + self.lastname + ' is Minor'

    def changeLastName(self, newlastname):
        self.lastname = newlastname


pid01 = Patient('Huzaifa', 'Ahmed', 20)
pid01.checkMinor()
pid01.changeLastName('Ahmeds')

# print pid01.lastName

# pid02 = Patient('osama')
# pid03 = Patient('adil')

# print pid01
# print pid02
# print pid03
