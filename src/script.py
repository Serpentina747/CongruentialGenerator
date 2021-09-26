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

# Funció que encripta una línia i la retorna en forma de cadena de caràcters
def encriptar_linia(linia, a, c):

    linia_encriptada = ""
    for caracter in range(0, len(linia)):
        if(linia[caracter].isupper()):
            resultat = ((a + alphabet_list_up.index(linia[caracter])) * c) % 26
            linia_encriptada = linia_encriptada + alphabet_list_up[resultat]
        elif(linia[caracter].islower()):
            resultat = ((a + alphabet_list.index(linia[caracter])) * c) % 26
            linia_encriptada = linia_encriptada + alphabet_list[resultat]
        else:
            linia_encriptada = linia_encriptada + linia[caracter]
    return linia_encriptada

# Funció que desencripta una línia i la retorna en forma de cadena de caràcters
def desencriptar_linia(linia, a, c):

    linia_desencriptada = ""
    for caracter in range(0, len(linia)):
        if(linia[caracter].isupper()):
            resultat = ((alphabet_list_up.index(linia[caracter]) / c) - a) % 26
            linia_desencriptada = linia_desencriptada + alphabet_list_up[resultat]
        elif(linia[caracter].islower()):
            resultat = ((alphabet_list.index(linia[caracter]) / c) / - a) % 26
            linia_desencriptada = linia_desencriptada + alphabet_list[resultat]
        else:
            linia_desencriptada = linia_desencriptada + linia[caracter]
    return linia_desencriptada



# Funció principal
def main():

    ruta = ".\\data\\"
    # Llegim l'input de l'usuari

    a = 2 # a = input("Coeficient a: ")
    c = 3 # c = input("Coeficient c: ")
    # s = input("Llavor s: ")
    nomFitxer = "fitxer1.txt" #input("Nom fitxer: ")
    nomFitxer_xifrat = "fitxer_xifrat.txt"
    nomFitxer_desxifrat = "fitxer_desxifrat.txt"

    ruta_xifrat = ruta + nomFitxer_xifrat
    ruta_desxifrat = ruta + nomFitxer_desxifrat
    ruta = ruta + nomFitxer

    if not os.path.isfile(ruta):
        print("El fitxer no existeix")
        quit()

    # Llegim el fitxer i obriem el fitxer amb el text encriptat
    fitxer = open(ruta, 'r')
    fitxer_xifrat = open(ruta_xifrat, 'w')
    linies = fitxer.readlines()

    # Encriptem el text normal del fitxer i el disposem dins d'un segon fitxer
    for linia in linies:
        linia_encriptada = encriptar_linia(linia, a, c)
        print(linia_encriptada)
        fitxer_xifrat.write(linia_encriptada)

    fitxer_desxifrar = open(ruta_xifrat, 'r')
    fitxer_desxifrat = open(ruta_desxifrat, 'w')

    linies_xifrades = fitxer_desxifrar.readlines()

    # Desencriptem
        # linia_encriptada = desencriptar_linia(linia, a, c)
        # fitxer_desxifrat.write(linia_encriptada)


    fitxer.close()
    fitxer_xifrat.close()
    fitxer_desxifrar.close()
    fitxer_desxifrat.close()

if __name__ == '__main__':
    main()

