
import math

print("welcome to my OMNI-CALCULATOR 5000")

vmntis=1
while vmntis == 1:
    calc_choice = input ("Which Calculator Would You Like To Use?")
    if calc_choice == "time dialation" or calc_choice == "td":
        print ("Welcome to my time dialation calculator!")
        c = 299792458
        v = int(input("What is the velocity you are traveling at? (in m/s rounded to the nearest whole number)"))
        t = int(input("How long will you be traveling at this speed (to the nearest whole number)(the output unit will be the same as the input unit)"))

        td = t * (math.sqrt(1 - v**2 / c**2))

        print (td)
    if calc_choice == "division" or calc_choice == "div" or calc_choice == "/":
        inpdiv = (int(input("what are you dividing?")))
        inpdivby = (int(input("what do you want to divide it by?")))
        stp1 = inpdiv // inpdivby
        rem = inpdiv % inpdivby
        divnr2 = inpdiv / inpdivby
        print (stp1)
        print ("Remainder ", rem)
        print ("As A Decimal: ", divnr2)
    if calc_choice == "subtract" or calc_choice == "sub" or calc_choice == "-":
        mainsubnum = int(input("what do you want to subtract?"))
        mainsubnumby = int(input("what do you want to subtract from it?"))
        anssub1 = mainsubnum - mainsubnumby
        print(anssub1)
    if calc_choice == "add" or calc_choice == "+":
        addin1 = int(input("what do you want to add to?"))
        addin2 = int(input("what do you want to add to it?"))
        addtot = addin1 + addin2
        print(addtot)
    if calc_choice == "multiply" or calc_choice == "*":
        inpmult = int(input("what is the number you want to multiply?"))
        inpmultby = int(input("what do you want to multiply it by"))
        multtot = inpmult * inpmultby
        print(multtot)
    if calc_choice == "arithmetic sequence" or calc_choice == "asq":
        asn = int(input ('please enter the part of the sequence you are trying to find'))
        asr_raw1 = int(input ('please enter the first number in the sequence'))
        asr_raw2 = int(input ('please enter the second number in the sequence'))
        asa1 = asr_raw1
        asr_solved = asr_raw2 - asr_raw1
        asstep_1 = asa1 + asr_solved*(asn - 1)
        print (asstep_1)
    if calc_choice == "download" or calc_choice == "download time" or calc_choice == "dt":
        print ("Welcome to my download time caculator!")
        dspeed = (float(input ("what is the speed of the download? (in MB/s)")))
        dsize = (float(input ("what is the size of the download?(in GB)")))
        dmb = dsize * 1000
        dseconds1 = dmb / dspeed
        dminutes = dseconds1 / 60
        dseconds2 = dseconds1 % 60
        dhours = dminutes / 60
        dminutes2 = dminutes % 60
        dminutesr = math.floor(dminutes2)
        dhoursr = math.floor(dhours)
        dsecondsr = math.floor(dseconds2)
        print (dhoursr,"hours", dminutesr,"Minutes " ,dsecondsr,"Seconds")
    if calc_choice == "tax" or calc_choice == "sales tax" or calc_choice == "stx":
        print ("Welcome To Henri's Sales Tax Calculator")
        tstate = input ("What state do you live in?")
        if tstate == "MN" or "mn":
            price_mn = float (input ("please input the price of the item(s)"))
            mntax = price_mn * 0.06875
            mntotal = price_mn + mntax
            mntotalrnd = round(mntotal,2)
            print (mntotalrnd)
        if tstate == "NY" or "mn":
            price_ny = float (input ("please input the price of the item(s)"))
            nytax = price_ny * 0.08875
            nytotal = price_ny + nytax
            nytotalrnd = round(nytotal,2)
            print (nytotalrnd)
        else:
            print("sorry, I haven't implemented that state yet.")
    if calc_choice == "scientific" or calc_choice == "sci not" or calc_choice == "scin":
        calc1c = input ("are you converting to or from scientific notation?")
        if calc1c == "from":
            eqc = input ("does your equation contain a decimal point?")
            if eqc == "yes": 
                ans12 = float(input ("please enter everything on the left side of the x"))
                ans13 = int(input("please enter the exponent"))
                ansf2 = ans12 * 10 ** (ans13)
                print (ansf2)
            if eqc == "no":
                ans14 = int(input ("please enter everything on the left side of the x"))
                ans15 = int(input("please enter the exponent"))
                ansf3 = ans14 * 10 ** (ans15)
                print (ansf3)
        if calc1c == "to":
            eqc2 = input ("does your equation contain a decimal point?")
            if eqc2 == "yes":
                ans20 = float(input("please enter your number"))
                print(format(ans20, "10.2E"))
            if eqc2 == "no":
                ans21 = float(input("please enter your number"))
                print(format(ans21, "10.2E"))
    if calc_choice == "pythagorean theorem" or calc_choice == "pythag" or calc_choice == "pt":
        pa = float(input("please enter the length of leg 1"))
        pb = float(input("please enter the length of leg 2"))
        pa_2 = pa**2
        pb_2 = pb**2
        pc_2 = pa_2 + pb_2
        pc = math.sqrt(c_2)
        print(pc)
    if calc_choice == "geometric sequence" or calc_choice == "geo seq" or calc_choice == "gs":
        gn = int(input ('please enter the part of the sequence you are trying to find'))
        gr_raw1 = int(input ('please enter the first number in the sequence'))
        gr_raw2 = int(input ('please enter the second number in the sequence'))
        ga1 = int(input ('please enter the first number in the sequence again'))
        gr_solved = gr_raw2 / gr_raw1 
        gstep_1 = ga1 * gr_solved**(gn - 1)
        print (gstep_1)
    if calc_choice == "free living reverse" or calc_choice == "flr":
        flrmib = int(input ("how much money do you have in your bank account? (in US Dollars)"))
        flrintr = float(input("At what intrest rate?"))
        flrperc = (flrintr * flrmib) / 100
        flrmonth = flrperc / 12
        print (flrmonth)
    if calc_choice == "free living" or calc_choice == "flc":
        print ("Hello! Welcome to my Free Living Calculator")
        flmonthlyinc = int(input ("How much money do you want to have per month"))
        flintr = float(input ("At what intrest rate?"))
        flyearlyinc = flmonthlyinc * 12
        flint1 = flyearlyinc * 100
        flmib = flint1 / flintr
        flearn1 = flmib * 100
        flearn2 = flearn1 / 60
        print ("you need to have", flmib , "dollars in the bank", "and you need to earn", flearn2 , "dollars")
    if calc_choice == "binge calculator" or calc_choice == "binge" or calc_choice == "bc":
        bcnumep = (int(input("How Many Episodes Are There In The Show/Season/Arc You Want To Binge?")))
        bceptimeraw = (int(input("How Many Minutes Is Each Episode? (Round To The Nearest Whole Minute)")))
        bcrawtime = bceptimeraw * bcnumep
        bchours = bcrawtime // 60
        bcminutes = bcrawtime % 60
        print (bchours, " Hours, ", bcminutes, " Minutes")
    if calc_choice == "help":
        print("Calculators: division;'/', addition;'+', subtraction;'-', multiplication;'*', download time;'dt', pythagorean theorem;'pt', binge calculator;'bc', free living;'flc', free living reverse;'flr', geometric sequence;'gs', scientific notation;'scin', sales tax;'stx', arithmetic sequence;'asq', time dialation;'td'")
test1
