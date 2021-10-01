import os.path
import string
import sys
import unicodedata



# Encriptació a través d'un generador congruencial

# Lletres minúscules i majúscules es consideren equivalents
# Espais, apòstrofs, xifres (de 0 a 9) i altres signes de puntuació no s'encripten
# Les lletres amb accent o especials s'assumiran sense accent (à -> a, ç -> c, ñ -> n)

alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)

alphabet_string_up = string.ascii_uppercase
alphabet_list_up = list(alphabet_string_up)

n_caracters_text_normal = 0 # Quantitat de caràcters del text normal
n_caracters_text_encriptat = 0 # Quantitat de caràcters del text encriptat

# Elimina tots els accents de el text entrat i retorna una cadena de caràcters amb el text processat
def normalitzar(text):
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3 
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)

# Funció que encripta una línia i la retorna en forma de cadena de caràcters
def encriptar_linia(linia, a, c):

    linia_encriptada = ""
    for caracter in range(0, len(linia)):
        if(linia[caracter].isupper()):
            caracter_normal = normalitzar(linia[caracter])
            resultat = ((a * alphabet_list_up.index(caracter_normal)) + c) % 26
            linia_encriptada = linia_encriptada + alphabet_list_up[resultat]
        elif(linia[caracter].islower()):
            caracter_normal = normalitzar(linia[caracter])
            resultat = ((a * alphabet_list.index(caracter_normal)) + c) % 26
            linia_encriptada = linia_encriptada + alphabet_list[resultat]
        else:
            linia_encriptada = linia_encriptada + linia[caracter]
    return linia_encriptada

# Funció que desencripta una línia i la retorna en forma de cadena de caràcters
def desencriptar_linia(linia, a, c):
    linia_desencriptada = ""
    for caracter in range(0, len(linia)):
        if(linia[caracter].isupper()):
            print("Majúscules: ", alphabet_list_up.index(linia[caracter]))
            resultat_mod_invers = pow(alphabet_list_up.index(linia[caracter]), -1, 26)
            resultat = int((resultat_mod_invers - c) / a)
            linia_desencriptada = linia_desencriptada + alphabet_list_up[resultat]
        elif(linia[caracter].islower()):
            print("Minúscules: ", alphabet_list.index(linia[caracter]))
            resultat_mod_invers = pow(alphabet_list.index(linia[caracter]), -1, 26)
            print(resultat_mod_invers)
            resultat = int((resultat_mod_invers - c) / a)
            linia_desencriptada = linia_desencriptada + alphabet_list[resultat]
        else:
            linia_desencriptada = linia_desencriptada + linia[caracter]
    return linia_desencriptada

# Funció que a partir d'una línia, treus els accents de totes les lletres que en porten, i retorna una cadena de caràcters amb aquests sense accents
def normalitzar_linia(linia):
    linia_normalitzada = ""
    for caracter in range(0, len(linia)):
        if(linia[caracter].isupper()):
            caracter_normal = normalitzar(linia[caracter])
            linia_normalitzada = linia_normalitzada + caracter_normal
        elif(linia[caracter].islower()):
            caracter_normal = normalitzar(linia[caracter])
            linia_normalitzada = linia_normalitzada + caracter_normal
        else:
            linia_normalitzada = linia_normalitzada + linia[caracter]
    return linia_normalitzada


def generar_sequencia(a,c,s):
    llista_enters = []
    llista_enters.append(s)
    existeix_repetit = False
    x = s
    while not existeix_repetit:
        resultat = ((a * x) + c) % 26
        if resultat in llista_enters:
            existeix_repetit = True
            break
        llista_enters.append(resultat)
        x = resultat

    print(llista_enters)
    print("Periode: ", len(llista_enters))

# Funció que compta els caràcters que no són ni comes, ni punts, ni cometes ni espais en blanc
def comptar_lletres(linies, textNormal):
    global n_caracters_text_normal
    global n_caracters_text_encriptat
    for linia in linies:
        for caracter in range(0, len(linia)):
            if(linia[caracter].isupper()):
                if (textNormal):
                    n_caracters_text_normal = n_caracters_text_normal + 1
                else:
                    n_caracters_text_encriptat = n_caracters_text_encriptat + 1
            elif(linia[caracter].islower()):
                if (textNormal):
                    n_caracters_text_normal = n_caracters_text_normal + 1
                else:
                    n_caracters_text_encriptat = n_caracters_text_encriptat + 1
# Funció principal
def main():

    ruta = ".\\data\\"
    # Llegim l'input de l'usuari

    a = 2 # a = input("Coeficient a: ")
    c = 6 # c = input("Coeficient c: ")
    
    s = int(input("Llavor s: "))

    nomFitxer = "fitxer1.txt" #input("Nom fitxer: ")
    nomFitxer_xifrat = "fitxer_xifrat.txt"
    nomFitxer_desxifrat = "fitxer_desxifrat.txt"

    ruta_xifrat = ruta + nomFitxer_xifrat
    ruta_desxifrat = ruta + nomFitxer_desxifrat
    ruta = ruta + nomFitxer

    # Generem la seqüència de valors enters amb el generador congruencial (ax+c mod L) a partir de la llavor 's', indiquem també el període de la seqüència
    generar_sequencia(a,c,s)


    if not os.path.isfile(ruta):
        print("El fitxer no existeix")
        quit()

    # Llegim el fitxer i obriem el fitxer amb el text encriptat
    fitxer = open(ruta, 'r', encoding='utf-8')
    fitxer_xifrat = open(ruta_xifrat, 'w')
    linies = fitxer.readlines()

    fn = open('normalitzat.txt', 'w')

    # Comptem les línies del text sense normalitzar ni encriptar
    comptar_lletres(linies, True)

    for linia in linies:
        linia_normal = normalitzar_linia(linia)
        fn.write(linia_normal)

    print("Nombre totals de caràcters del text normal: ", n_caracters_text_normal)
    # Encriptem el text normal del fitxer i el disposem dins d'un segon fitxer
    for linia in linies:
        linia_encriptada = encriptar_linia(linia, a, c)
        fitxer_xifrat.write(linia_encriptada)


    fitxer_xifrat.close()


    fitxer_desxifrar = open(ruta_xifrat, 'r')
    fitxer_desxifrat = open(ruta_desxifrat, 'w')

    linies_xifrades = fitxer_desxifrar.readlines()

    # Comptem les línies del text encriptat
    comptar_lletres(linies_xifrades, False)
    print("Nombre totals de caràcters del text encriptat: ", n_caracters_text_encriptat)
    # Desencriptem
    #for linia_encriptada in linies_xifrades:
        #print(linia_encriptada)
        #linia_desencriptada = desencriptar_linia(linia_encriptada, a, c)
        #fitxer_desxifrat.write(linia_desencriptada)

    

    fitxer.close()
    fitxer_desxifrar.close()
    fitxer_desxifrat.close()
    fn.close()

if __name__ == '__main__':
    main()

