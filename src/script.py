import os.path
import string
import sys
import unicodedata
from collections import Counter


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

llista_lletres_text_normal = ""
llista_lletres_text_encriptat = ""


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
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
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
    try:
        for caracter in range(0, len(linia)):
            if(linia[caracter].isupper()):
                resultat_mod_invers = modinv(a, 26) #pow(alphabet_list_up.index(linia[caracter]), -1, 26)
                resultat = (resultat_mod_invers * (alphabet_list_up.index(linia[caracter]) - c)) % 26 #resultat = int((resultat_mod_invers - c) / a)
                linia_desencriptada = linia_desencriptada + alphabet_list_up[resultat]
            elif(linia[caracter].islower()):
                resultat_mod_invers = modinv(a, 26) # pow(alphabet_list.index(linia[caracter]), -1, 26)
                resultat = (resultat_mod_invers * (alphabet_list.index(linia[caracter]) - c)) % 26#resultat = int((resultat_mod_invers - c) / a)
                linia_desencriptada = linia_desencriptada + alphabet_list[resultat]
            else:
                linia_desencriptada = linia_desencriptada + linia[caracter]
    except:
        print("No es pot desencriptar el text")
        quit()
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
    global llista_lletres_text_normal
    global llista_lletres_text_encriptat
    for linia in linies:
        for caracter in range(0, len(linia)):
            if(linia[caracter].isupper()):
                if (textNormal):
                    n_caracters_text_normal = n_caracters_text_normal + 1
                    caracter_minuscules = linia[caracter].lower()
                    caracter_normal = normalitzar(caracter_minuscules)
                    llista_lletres_text_normal = llista_lletres_text_normal + caracter_normal
                else:
                    n_caracters_text_encriptat = n_caracters_text_encriptat + 1
                    caracter_minuscules = linia[caracter].lower()
                    caracter_normal = normalitzar(caracter_minuscules)
                    llista_lletres_text_encriptat = llista_lletres_text_encriptat + caracter_normal
            elif(linia[caracter].islower()):
                if (textNormal):
                    n_caracters_text_normal = n_caracters_text_normal + 1
                    caracter_normal = normalitzar(linia[caracter])
                    llista_lletres_text_normal = llista_lletres_text_normal + caracter_normal
                else:
                    n_caracters_text_encriptat = n_caracters_text_encriptat + 1
                    caracter_normal = normalitzar(linia[caracter])
                    llista_lletres_text_encriptat = llista_lletres_text_encriptat + caracter_normal


# Funció que calcula l'índex de coincidencia
def calcular_index(res, TextNormal):
    n_parells_iguals = 0
    for lletres in alphabet_list:
        n_parells_iguals = n_parells_iguals + (res[lletres] * (res[lletres]-1))
    
    if(TextNormal): return (len(res)*(n_parells_iguals))/((n_caracters_text_normal)*(n_caracters_text_normal-1))
    else: return (len(res)*(n_parells_iguals))/((n_caracters_text_encriptat)*(n_caracters_text_encriptat-1))
        
# Funció principal
def main():

    ruta = ".\\data\\"
    # Llegim l'input de l'usuari

    a = 1 # a = input("Coeficient a: ") 
    c = 3 # c = input("Coeficient c: ") # Un nombre que ha de ser coprimer amb 26: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25... 
    
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

    # Llegim el fitxer i obrirem el fitxer amb el text a encriptar
    fitxer = open(ruta, 'r', encoding='utf-8')
    fitxer_xifrat = open(ruta_xifrat, 'w')
    linies = fitxer.readlines()

    fn = open('normalitzat.txt', 'w')

    # Comptem les lletres i la seva freqüència del text sense normalitzar ni encriptar
    comptar_lletres(linies, True)

    res1 = Counter(llista_lletres_text_normal)
    index_text_normal = calcular_index(res1, True)

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

    # Comptem les lletres i la seva freqüència del text encriptat
    comptar_lletres(linies_xifrades, False)

    res2 = Counter(llista_lletres_text_encriptat)
    index_text_encriptat = calcular_index(res2, False)


    print("Taula de freqüència del text normal: ", res1)
    print("Index coincidencia text normal: ", index_text_normal)
    print("Taula de freqüència del text desencriptat: ", res2)
    print("Index coincidencia text normal: ", index_text_encriptat)


    print("Nombre totals de caràcters del text encriptat: ", n_caracters_text_encriptat)


    # Desencriptem
    for linia_encriptada in linies_xifrades:
        linia_desencriptada = desencriptar_linia(linia_encriptada, a, c)
        fitxer_desxifrat.write(linia_desencriptada)

    


    fitxer.close()
    fitxer_desxifrar.close()
    fitxer_desxifrat.close()
    fn.close()

if __name__ == '__main__':
    main()

