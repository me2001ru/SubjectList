import datetime
import time
import json


class FileClassObject:

    def __init__(self, person_list=None):
        if person_list is None:
            self.person_list = []
        else:
            self.person_list = person_list


class Person(FileClassObject):
    def __init__(self, fname, lname, dob):
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.alias = self.fname[:2] + self.lname[:2] + self.dob[2:4]

    def __str__(self):
        # calculte age for person object + print person object
        now = datetime.datetime.now()
        year_born = (self.dob)[:4]
        return "{:<12}{:<12}{:<12}{:<7}{:<12}".format(self.fname, self.lname, self.dob, now.year - int(year_born), self.alias)


def add_user(person_listing, lan_id_list):
    # create object prompt
    user_input = (input("Give firstname, lastname and dob yyyymmdd\n>>").strip()).split(" ")

    # person has to be of age 18 and max 120 yr old.
    now = datetime.datetime.now()
    if 1900 < int(user_input[2][:4]) < now.year-17:
        # create object + add to file and lan_id_list
        new_user = Person(user_input[0], user_input[1], user_input[2])
        person_listing.append(new_user)
        lan_id_list.append(new_user.alias)
    else:
        print("Person to young/old for register. Addition N/A.")


def print_listing(person_listing):

    if len(person_listing) == 0:
        print("List is empty")
    else:
        print("{:<12}{:<12}{:<12}{:<7}{:<12}\n".format("FNAME", "LNAME", "DOB", "AGE", "LANID"))
        for individual in person_listing:
            print(individual)


def delete_user(person_listing, lan_id_list):
    # remove profile
    delete_who = input("enter user LANID for removal\n>>")

    # print user profile with this lanid
    for individual in person_listing:
        user_atb = list(individual.__dict__.values())
        if delete_who in user_atb:
            print("\nfound user: ", user_atb)

            confirmation = input("\nDelete this profile? Y/N:\n>>").upper()
            if confirmation == "Y":
                person_listing.remove(individual)


def quit_app(person_listing):
    data = {}
    data["people"] = []

    def ok(individual):
        individual = individual.__dict__
        return individual

    for individual in person_listing:
        okok = ok(individual)
        data["people"].append(okok)

    with open("data.txt", "w") as output_file:
        json.dump(data, output_file, indent=4)


def quit_program(person_listing):
    if len(person_listing) > 0:
        quit_app(person_listing)

        print("QUITING", end="")

        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(0.3)
        print()


def main():
    # instatiate File class- creates list.
    create_file = FileClassObject()

    # load list of data in and convert to objects.
    with open("data.txt", "r") as input_file:
        data = json.load(input_file)

        for an_object in data["people"]:
            attribute_list = list(an_object.values())
            create_file.person_list.append(Person(attribute_list[0], attribute_list[1], attribute_list[2]))

    # create lan_id_list
    lan_id_list = []
    for individual in create_file.person_list:
        individual_attributes = list(individual.__dict__.values())
        lan_id_list.append(individual_attributes[3])

    # through menu, while user not want out
    print("\nWelcome".upper())
    user_continue = True
    while user_continue:
        try:
            user_choice = int(input("\n-OPTION MENU-\n0.Save and quit, press\n1.Add person\n2.print file\n3.Delete user\n>>"))
        except Exception:
            print("wrong key...")
            continue

        if user_choice == 1:
            add_user(create_file.person_list, lan_id_list)

        elif user_choice == 2:
            print_listing(create_file.person_list)

        elif user_choice == 3:
            delete_user(create_file.person_list, lan_id_list)

        elif user_choice == 0:
            quit_program(create_file.person_list)
            user_continue = False

        else:
            print("N/A")


if __name__ == "__main__":
    main()
