import os.path
import string

# Encriptació a través d'un generador congruencial

# Lletres minúscules i majúscules es consideren equivalents
# Espais, apòstrofs, xifres (de 0 a 9) i altres signes de puntuació no s'encripten
# Les lletres amb accent o especials s'assumiran sense accent (à -> a, ç -> c, ñ -> n)

alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)

alphabet_string_up = string.ascii_uppercase
alphabet_list_up = list(alphabet_string_up)


def encriptar_linia(linia, a, c):

    print(linia)
    for caracter in range(0, len(linia)):
        print(linia[caracter])
        print(alphabet_list.index(linia[caracter]))
    return " "



def main():

    ruta = ".\\data\\"
    # Llegim l'input de l'usuari

    a = 5 # a = input("Coeficient a: ")
    c = 7 # c = input("Coeficient c: ")
    # s = input("Llavor s: ")
    nomFitxer = "fitxer1.txt" #input("Nom fitxer: ")
    ruta = ruta + nomFitxer
    if not os.path.isfile(ruta):
        print("El fitxer no existeix")
        quit()
    # Llegim el fitxer


    fitxer = open(ruta, 'r')
    linies = fitxer.readlines()

    print(linies)
    
    for linia in linies:
        linia_encriptada = encriptar_linia(linia, a, c)

if __name__ == '__main__':
    main()

