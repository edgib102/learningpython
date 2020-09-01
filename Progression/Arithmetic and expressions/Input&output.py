def createPerson():
    person = dict()
    person["Name"] = input("Enter name: ")
    person["Age"] = input("Enter age: ")
    person["Job"] = input("Enter job: ")
    print(person)

while True:
    print("Do you want to add a person?")
    yN = input("y/n: ")
    if yN == "y":
        createPerson()
    else:
        print("Quit?")
        quit_Yn = input("y/n: ")
        if quit_Yn == "y":
            quit()

#not sure how to add multiple people but this will do

            