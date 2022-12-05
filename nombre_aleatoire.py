#Auteur : Clervil WIlky

import random

jwe = 1

while jwe==1:
    nonb_odinate = random.randrange(0,500)
    print(nonb_odinate)
    pedi = True
    for i in range(5):
        print("ou rete ",5-i," chans")
        print("bon nonb lan antre 0 e 500")
        nonb_chwazi = int(input("ki nonb ou chwazi itilizate? "))
        
        if nonb_chwazi>nonb_odinate :
            print("nonb ou chwazi s tro gran")

        if nonb_chwazi<nonb_odinate :
            print("nonb ou chwazi a tro piti")

        if nonb_chwazi==nonb_odinate :
            print("bwavo!!! ou genyen")
            pedi = False
            break
        print("\n")

    if pedi :
        print("Ou pedi, bon nonb lan se ",nonb_odinate)
        
    jwe = int(input("Peze 1 si ou vle kontinye :"))
    print("\n")
