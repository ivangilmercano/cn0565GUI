from src import CN0565

fpos = 22
fneg = 23
temp = fpos - fneg
# 0 - eight, 1 - sixteen, 2 - twenty-four
elec = 2

opType=CN0565(fpos, fneg)

# eight electrodes
if elec == 0:
    if temp == -1 or temp == 7:
        f_function = opType.adjacent8()
        print("adjacent")
        print(f_function)
    elif temp == 4 or temp == -4:
        f_function = opType.adjacent8()
        print("opposite")
        print(f_function)
    else:
        print("fpos and fneg is not valid!")

# sixteen electrodes
elif elec == 1:
    if temp == -1 or temp == 16:
        f_function = opType.adjacent16()
        print("adjacent")
        print(f_function)
    elif temp == 8 or temp == -8:
        f_function = opType.adjacent16()
        print("opposite")
        print(f_function)
    else:
        print("fpos and fneg is not valid!")

# twenty-four electrodes
elif elec == 2:
    if temp == -1 or temp == 24:
        f_function = opType.adjacent24()
        print("adjacent")
        print(f_function)
    elif temp == 12 or temp == -12:
        f_function = opType.adjacent24()
        print("opposite")
        print(f_function)
    else:
        print("fpos and fneg is not valid!")
    

