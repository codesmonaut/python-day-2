# # Uslovno grananje

# broj_tekst = input("Unesite trocifreni broj: ")

# broj_slova_u_tekstu = len(broj_tekst)

# if broj_slova_u_tekstu != 3:
#     print("Morate uneti trocifreni broj")
#     print("Program ce se iskljuciti...")
#     exit()
# else:
#     print("Uneli ste validan broj.")
#     print(broj_tekst[-1::-1])
#     print("Kraj programa.")

# # Zadatak sa brutom

# bruto = float(input("Unesite bruto iznos: "))

# # Gard
# if bruto < 60000:
#     print("Bruto iznos ne moze biti manji od 60000 RSD")
#     exit()

# porez = bruto * 0.1
# pio = bruto * 0.15
# rfzo = bruto * 0.07
# soc = bruto * 0.0075

# doprinosi = porez + pio + rfzo + soc

# neto = bruto - doprinosi

# print(f"Neto iznos je: {neto:.2f} RSD")

# # Formiranje ocene

# poeni = float(input("Unesite broj poena studenta: "))

# if poeni < 51:
#     print("Pao")
# elif poeni < 61:
#     print("6")
# elif poeni < 71:
#     print(7)
# elif poeni < 81:
#     print(8)
# elif poeni < 91:
#     print(9)
# else:
#     print(10)

# # Petlje/Ciklusi

# broj = int(input("Koliko puta zelite da Vam kazem dobar dan?"))

# for i in range(broj):
#     redni_broj = i + 1
#     print(f"Dobar dan {redni_broj}. put")

# print("Kraj programa")

# # Izracunati zbir svih brojeva od 2 do N.

# n = int(input("Unesite vrednost za N: "))

# if n < 2:
#     print(2)

# if n >= 2:
#     zbir = 0

#     # for broj in range(2, n + 1):
#     #     zbir += broj
#     #     print(f"Medjuzbir u ovom ciklusu je {zbir}...")

#     # print(zbir)

#     broj = 2

#     while broj <= n:
#         zbir += broj
#         broj += 1

#     print(zbir)

# # Izracunati zbir svakog drugog broja dokle god je zbir manji od 1000

# zbir = 0
# broj = 0

# while True:

#     if zbir + broj >= 1000:
#         break

#     zbir += broj
#     broj += 2

# print(zbir)

# # Papir, kamen, makaze

# broj_pobeda_igraca_1 = 0
# broj_pobeda_igraca_2 = 0

# for i in range(3):
#     odluka_igraca_1 = input(f"Ponavljanje {i + 1}. Igrac 1 je igrao: ")
#     odluka_igraca_2 = input(f"Ponavljanje {i + 1}. Igrac 2 je igrao: ")

#     if odluka_igraca_1 == "P" and odluka_igraca_2 == "K":
#         broj_pobeda_igraca_1 += 1
#     elif odluka_igraca_1 == "P" and odluka_igraca_2 == "M":
#         broj_pobeda_igraca_2 += 1
#     elif odluka_igraca_1 == "K" and odluka_igraca_2 == "M":
#         broj_pobeda_igraca_1 += 1
#     elif odluka_igraca_1 == "K" and odluka_igraca_2 == "P":
#         broj_pobeda_igraca_2 += 1
#     elif odluka_igraca_1 == "M" and odluka_igraca_2 == "K":
#         broj_pobeda_igraca_2 += 1
#     elif odluka_igraca_1 == "M" and odluka_igraca_2 == "P":
#         broj_pobeda_igraca_1 += 1

# if broj_pobeda_igraca_1 == broj_pobeda_igraca_2:
#     print("Igra je neresena!")
# elif broj_pobeda_igraca_1 > broj_pobeda_igraca_2:
#     print("Igrac 1 je pobedio")
# elif broj_pobeda_igraca_1 > broj_pobeda_igraca_2:
#     print("Igrac 2 je pobedio")

# Napraviti program koji simulira meni kase

while True:
    print("Opcije menija su: ")
    print("  L - Lista svih stavki")
    print("  N - Nova stavka")
    print("  I - Izmena stavke")
    print("  B - Brisanje stavke")
    print("  O - Otvaranje racuna")
    print("  P - Prodaja - dodavanje stavke na racun")
    print("  S - Stampa racuna")
    print("  X - Izlaz iz programa")

    odluka = input("Izaberite opciju: ")

    if odluka == "X":
        print("Odlucili ste da iskljucite program.")
        print("Program se iskljucuje...")
        break
    elif odluka == "L":
        print("Listam stavke...")
    elif odluka == "N":
        print("Dodajem stavku...")
    elif odluka == "I":
        print("Menjam stavku...")
    elif odluka == "B":
        print("Brisem stavku...")
    elif odluka == "O":
        print("Otvaram racun")
    elif odluka == "P":
        print("Dodajem stavku na racun")
    elif odluka == "S":
        print("Stampam racun")
    else:
        print("Unesite jednu od ponudjenih opcija: ")

print("Zakljucimo dan.")