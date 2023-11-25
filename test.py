d1 = {'a': 101, 'b': 202, 'c':300}
d2 = {'a': 303, 'b': 201, 'd':402}

d3={}
b=[]
for elemt in d2.keys():
    for elmt in d1.keys():
        if elmt == elemt :
            a=d1[elmt]+d2[elemt]
            b.append (a)
        elif elemt not in d1.keys():
            a = d2[elemt]
    if elmt not in d2.keys():
        a = d1[elmt]
    print (a)
print(b)

