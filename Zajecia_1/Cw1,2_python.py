temp = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym.' \
       ' Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. ' \
       'Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. ' \
       'Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty' \
       ' Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym ' \
       'do realizacji druków na komputerach osobistych, jak Aldus PageMaker'

imie = 'Rafal'
nazwisko = 'Kurenda'

litera_1 = imie[2]
litera_2 = nazwisko[3]

count_1 = 0
count_2 = 0



for i in temp:
    if i == litera_1:
        count_1 = count_1 + 1
    else:
        count_2 = count_2 + 1

print("W tekście jest " + str(count_1) + " liter " + str(litera_1) + " oraz " + str(count_2) + " liter " + str(litera_2))
