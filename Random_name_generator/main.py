import random

def name():
    first_names = ['Jeremy', 'James', 'Richard', 'Meghan', 'Piers']
    last_names = ['Clarkson', 'May', 'Hammond', 'Markle', 'Morgan']

    print(random.choice(first_names), random.choice(last_names))

name()
    
option = ''

while option != "N":
    option = input("Generate another name? (Y/N) ").upper()
    if option == "Y":
        print("")
        name()
