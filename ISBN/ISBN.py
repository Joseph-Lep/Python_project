#probleme luhn_calc incompatible avec création et validation 
# --> résolvable en suppr l'index 0 une fois la list renversée et avance appel luhn_calc
#problème fonctions, ne pas définir des variables en global
#problème "V" et "Q" non pris en compte

check_digit = 0
isbn = 0
arr_isbn = None
odd_index = 0
even_index = 0
sumofall = 0
Number = 0
Index = None
loopsum = 0
choice = ""

def luhn_calc():
    for Index ,Number in enumerate(arr_isbn):
        if (Index)%2 != 0:
            odd_index = Number*1
            loopsum += odd_index
        else:
            even_index = Number*3
            loopsum += even_index
    if Index>=11:
        check_digit = loopsum%10
        check_digit = 10 - check_digit
        arr_isbn.reverse()

def correct(): 
    try:
        isbn = int(isbn)
    except ValueError:
        print("Veuillez rentrer une suite de nombres valide, pas de charateres ou d'espaces")
        exit()

print("""
Bonjour, bienvenue sur ce logiciel de création et de vérification d'ISBN-13
Que souhaitez vous faire ?
      """)
choice = str(input("""
                   C : pour crée une clé ISBN
                   V : pour vérifier si l'ISBN est correct
                   Q : pour quitter 
                   """))
choice = choice.upper()
while choice != "C" and "V" and "Q":
    print("Navré, il n'y a que 3 commandes possibles")
    choice = str(input("""
                   C : pour crée une clé d'ISBN
                   V : pour vérifier si l'ISBN est correct
                   Q : pour quitter 
                   """))
    choice = choice.upper()
if choice == "Q":
    print("Goodbye !")
    exit()
elif choice == "C":
    isbn = input("Veuillez rentrer une série de 12 chiffres svp : ")
    arr_isbn = [int(digit) for digit in str(isbn)]
    arr_isbn.reverse()
    luhn_calc()
    print(arr_isbn, check_digit)
elif choice == "V":
    arr_isbn = [int(digit) for digit in str(isbn)]
    arr_isbn.reverse()
    isbn = input("Veuillez rentrer votre ISBN complet (13 chiffres) : ")
    luhn_calc()
    print(arr_isbn)