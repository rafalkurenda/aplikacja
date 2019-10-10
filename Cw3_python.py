name = "imie"
surname = "nazwisko"
number = 1997
data = {'first' : 'haha', 'last': "hahalast"}


print('{:>30}'.format(surname))
print('{:_>30}'.format(surname))
print('{:^10}'.format(name))
print('{:0.3f}'.format(1997))
print('{first} {last}'.format(**data))