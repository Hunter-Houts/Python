class Person:
    name = ""
    age = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sayHello(self):
        print("Hello from {}".format(self.name))

    def ageWhen100(self):
        print("You are currently {} and you will be 100 in the year {}".format(self.age,(2018-self.age)+100))

    def work(self,typeOfWork):
        print("{} is {}".format(self.name,typeOfWork))

    def sleep(self):
        print("{} is sleeping".format(self.name))

# Houses hold people


class House(Person):
    people = []
    houseName = ""

    def __init__(self,houseName):
        super()
        self.houseName = houseName
        self.people = []

    def getHouseName(self):
        return self.houseName

    def addPerson(self,Person):
        self.people.append(Person)

    def numOfPeople(self):
        if(len(self.people) > 1):
            print("There are {} people in the {} House".format(len(self.people),self.houseName))
        elif(len(self.people) == 1):
            print("There is {} person in the {} House".format(len(self.people),self.houseName))
        else:
            print("There is no one in the house")

    def ShowAllPeople(self):
        if(len(self.people) > 0):
            print("The {} people in the {} House are:".format(len(self.people),self.houseName))
            for p in self.people:
                print("Name: {}\nAge: {}".format(p.name,p.age))
                print("--------------------------------------")
        else:
            print("There is no one in the house")

    def cleanHouse(self):
        if(len(self.people) > 0):
            for p in self.people:
                print("{} is cleaning the house".format(p.name))
        else:
            print("There is no one to clean the house")

# Towns hold houses


class Town(House):
    town = []

    def __init__(self):
        super()
        self.town = []

    def addHouse(self,House):
        self.town.append(House)

    def numOfHouses(self):
        if(len(self.town) > 1):
            print("There are {} Households in the town".format(len(self.town)))
        elif(len(self.town) == 1):
            print("There is {} household in the town".format(len(self.town)))
        else:
            print("There are no households in the town")

    def nameAllPeopleInTown(self):
        print("The name of each person in town are as follows:")
        if(len(self.town) > 0):
            for h in self.town:
                print("In the {} Household,".format(h.getHouseName()))
                print(h.ShowAllPeople())


def main():
    Hunter = Person("Hunter", 22)
    Hunter.sayHello()
    Hunter.ageWhen100()
    Hunter.work("Coding")
    Hunter.sleep()
    B = Person("B", 21)
    B.sayHello()
    B.ageWhen100()
    B.work("Working hard")
    B.sleep()
    Dale = Person("Dale", 50)
    Jen = Person("Jen", 48)
    Dan = Person("Dan", 13)
    theHouse = House("M")
    House2 = House("H")
    House2.addPerson(Dale)
    House2.addPerson(Jen)
    House2.addPerson(Dan)
    theHouse.addPerson(B)
    theHouse.addPerson(Hunter)
    theHouse.numOfPeople()
    House2.numOfPeople()
    print("The People in the House are:")
    theHouse.ShowAllPeople()
    print()
    House2.ShowAllPeople()
    theHouse.cleanHouse()
    theTown = Town()
    theTown.addHouse(theHouse)
    theTown.addHouse(House2)
    theTown.numOfHouses()
    theTown.nameAllPeopleInTown()


if __name__ == "__main__":
    main()
