class CN0565():
    
    def __init__(self, fpos, fneg):
        self.fpos=fpos
        self.fneg=fneg
        #self.spos=spos
        #self.sneg=sneg
    ################################## FOR EIGHT ELECTRODES ###########################################
    def adjacent8(self):
        #initializing of lists
        main_list = [] #main container of each combination [[f+, f-],[s+,s-,...,s+,s-]]
        ftemp_list=[] #temporary container for f+ and f-
        stemp_list=[] #teporary container for s+ s-
        spos = 0
        sneg = 0

        for findex in range(0,8):
            ftemp_list.append("f")
            ftemp_list.append(self.fpos)
            ftemp_list.append(self.fneg)
            if self.fneg + 1 > 7:
                spos = 0
            else:
                spos = self.fneg +1
            sneg = spos + 1
            if sneg + 1 > 7:
                sneg=0
            else:
                sneg = spos +1

            for sindex in range(0,5):
                stemp_list.append("s")
                stemp_list.append(spos)
                stemp_list.append(sneg)
                if sneg >= 7:
                    sneg = 0
                else:
                    sneg = sneg + 1
                if spos >= 7:
                    spos = 0
                else:
                    spos = spos + 1

            if self.fneg >= 7:
                self.fneg = 0
            else:
                self.fneg = self.fneg + 1

            if self.fpos >= 7:
                self.fpos = 0
            else:
                self.fpos = self.fpos + 1

            main_list.append(ftemp_list)
            main_list.append(stemp_list)
            ftemp_list=[]
            stemp_list=[]
        return main_list

    def opposite8(self):
        #initializing of lists
        main_list = [] #main container of each combination [[f+, f-],[s+,s-,...,s+,s-]]
        ftemp_list=[] #temporary container for f+ and f-
        stemp_list=[] #teporary container for s+ s-

        #loop for f+ and f-
        for findex in range(0,8):
            ftemp_list.append("f")
            ftemp_list.append(self.fpos)
            ftemp_list.append(self.fneg)
            if self.fneg + 1 > 7:
                spos = 0
            else:
                spos = self.fneg +1
            sneg = spos + 1
            if sneg + 1 > 7:
                sneg=0
            else:
                sneg = spos +1

            #loop for s+ and s-
            checker=0
            stemp_list.append("s")
            while(checker<=3):
                if spos >=8:
                    spos =0
                if sneg >=8:
                    sneg=0
                if spos == self.fneg or spos == self.fpos:
                    spos = spos + 1
                    sneg = sneg + 1
                elif sneg == self.fneg or sneg == self.fpos:
                    spos = spos + 1
                    sneg = sneg + 1
                else:
                    stemp_list.append(spos)
                    stemp_list.append(sneg)
                    spos = spos +1
                    sneg = sneg +1
                    checker = checker+1
            #conditions for f+ and f-
            if self.fneg >= 7:
                self.fneg = 0
            else:
                self.fneg = self.fneg + 1

            if self.fpos >= 7:
                self.fpos = 0
            else:
                self.fpos = self.fpos + 1

            main_list.append(ftemp_list)
            main_list.append(stemp_list)
            ftemp_list=[]
            stemp_list=[]
        return main_list
    
    ############################################## FOR 16 ELECTRODES ###########################################
    def adjacent16(self):
        #initializing of lists
        main_list = [] #main container of each combination [[f+, f-],[s+,s-,...,s+,s-]]
        ftemp_list=[] #temporary container for f+ and f-
        stemp_list=[] #teporary container for s+ s-

        for findex in range(0,16):
            ftemp_list.append(self.fpos)
            ftemp_list.append(self.fneg)
            if self.fneg + 1 > 15:
                spos = 0
            else:
                spos = self.fneg +1
            sneg = spos + 1
            if sneg + 1 > 15:
                sneg=0
            else:
                sneg = spos +1

            for sindex in range(0,13):
                stemp_list.append(spos)
                stemp_list.append(sneg)
                if sneg >= 15:
                    sneg = 0
                else:
                    sneg = sneg + 1

                if spos >= 15:
                    spos = 0
                else:
                    spos = spos + 1

            if self.fneg >= 15:
                self.fneg = 0
            else:
                self.fneg = self.fneg + 1

            if self.fpos >= 15:
                self.fpos = 0
            else:
                self.fpos = self.fpos + 1

            main_list.append(ftemp_list)
            main_list.append(stemp_list)
            ftemp_list=[]
            stemp_list=[]
        return main_list

    def opposite16(self):
        #initializing of lists
        main_list = [] #main container of each combination [[f+, f-],[s+,s-,...,s+,s-]]
        ftemp_list=[] #temporary container for f+ and f-
        stemp_list=[] #teporary container for s+ s-

        #loop for f+ and f-
        for findex in range(0,16):
            ftemp_list.append("f")
            ftemp_list.append(self.fpos)
            ftemp_list.append(self.fneg)
            if self.fneg + 1 > 15:
                spos = 0
            else:
                spos = self.fneg +1
            sneg = spos + 1
            if sneg + 1 > 15:
                sneg=0
            else:
                sneg = spos +1

            #loop for s+ and s-
            checker=0
            stemp_list.append("s")
            while(checker<=11):
                if spos >=16:
                    spos =0
                if sneg >=16:
                    sneg=0
                if spos == self.fneg or spos == self.fpos:
                    spos = spos + 1
                    sneg = sneg + 1
                elif sneg == self.fneg or sneg == self.fpos:
                    spos = spos + 1
                    sneg = sneg + 1
                else:
                    stemp_list.append(spos)
                    stemp_list.append(sneg)
                    spos = spos +1
                    sneg = sneg +1
                    checker = checker+1
            #conditions for f+ and f-
            if self.fneg >= 15:
                self.fneg = 0
            else:
                self.fneg = self.fneg + 1

            if self.fpos >= 15:
                self.fpos = 0
            else:
                self.fpos = self.fpos + 1

            main_list.append(ftemp_list)
            main_list.append(stemp_list)
            ftemp_list=[]
            stemp_list=[]
        return main_list

    ############################################## FOR 24 ELECTRODES ###########################################
    def adjacent24(self):
        #initializing of lists
        main_list = [] #main container of each combination [[f+, f-],[s+,s-,...,s+,s-]]
        ftemp_list=[] #temporary container for f+ and f-
        stemp_list=[] #teporary container for s+ s-

        for findex in range(0,24):
            ftemp_list.append(self.fpos)
            ftemp_list.append(self.fneg)
            if self.fneg + 1 > 23:
                spos = 0
            else:
                spos = self.fneg +1
            sneg = spos + 1
            if sneg + 1 > 23:
                sneg=0
            else:
                sneg = spos +1

            for sindex in range(0,21):
                stemp_list.append(spos)
                stemp_list.append(sneg)
                if sneg >= 23:
                    sneg = 0
                else:
                    sneg = sneg + 1

                if spos >= 23:
                    spos = 0
                else:
                    spos = spos + 1

            if self.fneg >= 23:
                self.fneg = 0
            else:
                self.fneg = self.fneg + 1

            if self.fpos >= 23:
                self.fpos = 0
            else:
                self.fpos = self.fpos + 1

            main_list.append(ftemp_list)
            main_list.append(stemp_list)
            ftemp_list=[]
            stemp_list=[]
        return main_list

    def opposite24(self):
        #initializing of lists
        main_list = [] #main container of each combination [[f+, f-],[s+,s-,...,s+,s-]]
        ftemp_list=[] #temporary container for f+ and f-
        stemp_list=[] #teporary container for s+ s-

        #loop for f+ and f-
        for findex in range(0,24):
            ftemp_list.append("f")
            ftemp_list.append(self.fpos)
            ftemp_list.append(self.fneg)
            if self.fneg + 1 > 23:
                spos = 0
            else:
                spos = self.fneg +1
            sneg = spos + 1
            if sneg + 1 > 23:
                sneg=0
            else:
                sneg = spos +1

            #loop for s+ and s-
            checker=0
            stemp_list.append("s")
            while(checker<=19):
                if spos >=24:
                    spos =0
                if sneg >=24:
                    sneg=0
                if spos == self.fneg or spos == self.fpos:
                    spos = spos + 1
                    sneg = sneg + 1
                elif sneg == self.fneg or sneg == self.fpos:
                    spos = spos + 1
                    sneg = sneg + 1
                else:
                    stemp_list.append(spos)
                    stemp_list.append(sneg)
                    spos = spos +1
                    sneg = sneg +1
                    checker = checker+1
            #conditions for f+ and f-
            if self.fneg >= 23:
                self.fneg = 0
            else:
                self.fneg = self.fneg + 1

            if self.fpos >= 23:
                self.fpos = 0
            else:
                self.fpos = self.fpos + 1

            main_list.append(ftemp_list)
            main_list.append(stemp_list)
            ftemp_list=[]
            stemp_list=[]
        return main_list
if __name__ == "__main__":
    fpos = 22
    fneg = 23
    temp = fpos - fneg

    opType=CN0565(fpos, fneg)
    #if temp == -1 or temp == 7:
    #if temp == -1 or temp == 15:
    if temp == -1 or temp == 23:
        #f_function = opType.adjacent8()
        #f_function = opType.adjacent16()
        f_function = opType.adjacent24()
        print("adjacent")
        print(f_function)
    #elif temp == 4 or temp == -4:
    #elif temp == 8 or temp == -8:
    elif temp == 12 or temp == -12:
        #f_function = opType.opposite8()
        #f_function = opType.opposite16()
        f_function = opType.opposite24()
        print("opposite")
        print(f_function)
    else:
        print("fpos and fneg is not valid!")