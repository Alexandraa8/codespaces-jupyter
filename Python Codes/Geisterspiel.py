#Geisterspiel

from random import randint

print("Geisterspiel")
begruessung = 'Hallo'
name = input ('Wie heißt du? ')
begruessung = begruessung + ' ' + name + '.'
print(begruessung)

frage = input ('Wenn du bereit, drücke auf Enter!')
frage = frage + ' '
print(frage)

print("======================")

geist_gefunden = False
du_bist_mutig = True

Türanzahl = 0

while du_bist_mutig:
    geistertür = randint (1, 3)
    print (' ')
    print ('Vor dir sind insgesamt 3 Türen')
    print ('Hinter einer der drei Türen, ist der Geist versteckt')
    print ('Welche Tür öffnest du?')

    tür = input ('Öffne Tür 1, 2 oder 3')
    tuer_nummer = int

    if tuer_nummer == geistertür:
        print('Buuhh')
        




