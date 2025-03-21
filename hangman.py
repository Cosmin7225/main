#joc spanzuratorea
# M-as gandi la o lista de cuvinte definita din care sa alegem un cuvant aleaator
# Pc-ul alege un cuvant iar jucatorul trebuie sa ghiceasaca literele care alcatuiesc cuvantul
# Incercarile trebuie sa fie egale cu 6, deci trebuie o conditie (while) care verifica numarul de incercari iar la fiecare greseala nuamrul sa scada
# Apoi o conditie de verificare a literei alese, aceea de a fi in cuvantul selectat 
# daca este gresita se scade numarul de incercari iar daca este corecta se adauga

print('Acesta este jocul Hangman')
import random
lista_cuvinte=['python', 'pere', 'masina']
def hangman():
    cuvant_secret=random.choice(lista_cuvinte) #alegem un cuvant
    cuvant_ghicit=list('-'*len(cuvant_secret)) #introducem --- (intr-o lista) de un nr de ori egal cu lungimea cuvantului
    incercari=6 #numar de incercari limitat
    print(' '.join(cuvant_ghicit)) #afisez cuvantul - - - -

    while (incercari>0) and ('-' in cuvant_ghicit): #verific cat timp incercarile sunt mai mari ca 0
        litera=input(f'ghiceste o litera ').lower() #introduc litera
        if litera in cuvant_secret: 
            for i, lit in enumerate(cuvant_secret):
                if lit==litera:
                    cuvant_ghicit[i]=litera #aici folosesc enumerate pentru a ne da si indexul literi in cuvantul ghicit #si o afisez peste tot pe unde o gasesc
            print(f'jucatorul a ghicit litera iar litera {litera} este in cuvant') #daca litera e ghicita o afisez
        else:
            print(f"litera {litera} nu se gaseste in cuvant")
            incercari-=1 #daca n am gasit scad incercarile
        
        print(' '.join(cuvant_ghicit)) #printez cuvantul cu dupa multiplele incercari
        print(f"incercarile ramase sunt {incercari}")

        if '-' not in cuvant_ghicit:
            print(f"cuvantul a fost ghicit si este {''.join(cuvant_ghicit)}")
            break #daca cuvantul a fost ghicit ma opresc
    else:
        print(f"ai pierdut, cuvantul era {cuvant_secret}") #altfel jocul este pierdut pentru ca incercarile au fost finalizate
hangman()

