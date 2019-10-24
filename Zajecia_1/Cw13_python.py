lista = [{"a": "pies", "b":"kot", "c":"jeleń"}, {"d": "haha", "e":"hehe", "f":"hoho"}, {"g": "XD", "h":"XDD", "i":"XDDD"}]

string = ""

for i in lista:
    for x in i:
        string += str(x) + " "  + str(i[x] + " " )

print(string)
