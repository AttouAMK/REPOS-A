# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Demander le nom et l'age de l'utilisateur

nom = input("Quel est votre nom ? ")
age = input("Quel est votre age ? ")
print("Vous vous applez " + nom + ", vous avez " + age + " ans")

def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Entrer votre nom : ")
    return reponse_nom



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('AMK')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
