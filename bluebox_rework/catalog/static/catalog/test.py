import os



def fix(names):
    original = []
    new = []
    for i in names:
        if i[0] == "R":
            original.append(i)



    for i in names:
        if i[0] == "R":
            i = list(i)
            i[0] = ''
            i = ''.join(i)
            start, end = i.split(".")
            start = start + "R."
            name = start + end
            new.append(name)
    
    dictionary = dict(zip(original, new))


    for original, new in dictionary.items():
        os.rename(original, new)
names = (os.listdir())
fix(names)
