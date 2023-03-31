from src import CN0565

fpos = 7
fneg = 0
temp = fpos - fneg

opType=CN0565(fpos, fneg)
if temp == -1 or temp == 7:
#if temp == -1 or temp == 16:
#if temp == -1 or temp == 24:
    f_function = opType.adjacent8()
    #f_function = opType.adjacent16()
    #f_function = opType.adjacent24()
    print("adjacent")
    print(f_function)
elif temp == 4 or temp == -4:
#elif temp == 8 or temp == -8:
#elif temp == 12 or temp == -12:
    f_function = opType.adjacent8()
    #f_function = opType.adjacent16()
    #f_function = opType.adjacent24()
    print("opposite")
    print(f_function)
else:
    print("fpos and fneg is not valid!")