x = open("Info.txt", "a+")

def addNewPerson(name, age, gender):
    x.write(
    "\n"+"[" + name + "]"+"\n"
    + "Age: " + age + "\n" +
    "Gender: " + gender + "\n")

name = input("Enter name of new person:" + "\n")
age = input("Enter " + name + "'s age:" + "\n")
gender = input("Enter " + name + "'s gender:" + "\n")

addNewPerson(name, age, gender)