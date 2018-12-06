class Patient():
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def checkMinor(self):
        if self.age < 21:
            print self.firstName + ' ' + self.lastName + ' is Minor'

    def changeLastName(self, newLastName):
        self.lastName = newLastName


pid01 = Patient('Huzaifa', 'Ahmed', 20)
pid01.checkMinor()
pid01.changeLastName('Ahmeds')

# print pid01.lastName

# pid02 = Patient('osama')
# pid03 = Patient('adil')

# print pid01
# print pid02
# print pid03
