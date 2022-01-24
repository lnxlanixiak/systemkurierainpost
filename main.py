print ("Witaj w InPost!")
print ("Co robimy?")
print ("1- odbieranie paczki")
print ("2- nadanie paczki")
wybor = input()
if wybor == '1':
    print ("Ok! Podaj potrzebne dane! ")
    numer = input ("Podaj numer przesyłki")
    kod = input ("Podaj kod weryfikacyjny")
    if numer == '020420052137' and kod == '2137':
        print ("Przesyłka odebrana!")
        print ("Dziękujemy i zapraszamy ponownie!")

    else:print("Źle podany numer przesyłki lub kod weryfikacyjny")
if wybor == '2':
    print ("Ok! Podaj dane do wysyłki!")
    input ("Miasto:")
    input ("Kod pocztowy:")
    input ("Ulica i numer domu:")
    blik = input ("Do zapłaty: 8,00zl. Podaj kod BLIK:")
    if blik == '7312':
        print ("Paczka została nadana!")
    else:print("Źle podany BLIK")