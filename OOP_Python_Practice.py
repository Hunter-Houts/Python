class Person:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello from {}".format(self.name))

    def age_when100(self):
        print("You are currently {} and you will be 100 in the year {}".format(self.age, (2018-self.age)+100))

    def work(self,type_of_work):
        print("{} is {}".format(self.name, type_of_work))

    def sleep(self):
        print("{} is sleeping".format(self.name))

# Houses hold people


class House(Person):
    people = []
    houseName = ""

    def __init__(self, house_name):
        super()
        self.houseName = house_name
        self.people = []

    def get_house_name(self):
        return self.houseName

    def add_person(self, person):
        self.people.append(person)

    def num_of_people(self):
        if len(self.people) > 1:
            print("There are {} people in the {} House".format(len(self.people), self.houseName))
        elif len(self.people) == 1:
            print("There is {} person in the {} House".format(len(self.people), self.houseName))
        else:
            print("There is no one in the house")

    def show_all_people(self):
        if len(self.people) > 0:
            print("The {} people in the {} House are:".format(len(self.people), self.houseName))
            for p in self.people:
                print("Name: {}\nAge: {}".format(p.name, p.age))
                print("--------------------------------------")
        else:
            print("There is no one in the house")

    def clean_house(self):
        if len(self.people) > 0:
            for p in self.people:
                print("{} is cleaning the house".format(p.name))
        else:
            print("There is no one to clean the house")

# Towns hold houses.


class Town(House):
    town = []

    def __init__(self):
        super()
        self.town = []

    def add_house(self, House):
        self.town.append(House)

    def num_of_houses(self):
        if len(self.town) > 1:
            print("There are {} Households in the town".format(len(self.town)))
        elif len(self.town) == 1:
            print("There is {} household in the town".format(len(self.town)))
        else:
            print("There are no households in the town")

    def name_all_people_in_town(self):
        print("The name of each person in town are as follows:")
        if len(self.town) > 0:
            for h in self.town:
                print("In the {} Household,".format(h.get_house_name()))
                print(h.show_all_people())


def main():
    hunter = Person("Hunter", 22)
    hunter.say_hello()
    hunter.age_when100()
    hunter.work("Coding")
    hunter.sleep()
    b = Person("B", 21)
    b.say_hello()
    b.age_when100()
    b.work("Working hard")
    b.sleep()
    dale = Person("Dale", 50)
    jen = Person("Jen", 48)
    dan = Person("Dan", 13)
    the_house = House("M")
    house2 = House("H")
    house2.add_person(dale)
    house2.add_person(jen)
    house2.add_person(dan)
    the_house.add_person(b)
    the_house.add_person(hunter)
    the_house.num_of_people()
    house2.num_of_people()
    print("The People in the House are:")
    the_house.show_all_people()
    print()
    house2.show_all_people()
    the_house.clean_house()
    the_town = Town()
    the_town.add_house(the_house)
    the_town.add_house(house2)
    the_town.num_of_houses()
    the_town.name_all_people_in_town()


if __name__ == "__main__":
    main()
