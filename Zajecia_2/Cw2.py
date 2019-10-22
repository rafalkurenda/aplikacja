def text(data_text):

    slownik = {}

    lenght = len(data_text)
    slownik["Dlugosc"] = lenght

    letters = [i for i in data_text]
    slownik["Litery"] = letters

    big_letters = data_text.upper()
    slownik["Duze litery"] = big_letters

    small_letters = data_text.lower()
    slownik["Male litery"] = small_letters

    print(slownik)


temp = "Ala"


text(temp)