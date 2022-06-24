#!/usr/bin/python3
# from codecs import namereplace_errors
import sys
# from sympy import init_session
import sympy as sym
# from __future__ import division
from sympy import *

# how to import  library code exmple redirect out in file dump  file 
# library  context  blocks  >> stdout in file or alternate 
from contextlib import redirect_stdout
# import sympy
from sympy.abc import *
from sympy.parsing.sympy_parser import *
import math
import time

# init_session()x


def banner():
    syym ="""
        '#################################'
        ' ___ _   _ _ __ ___  _ __  _   _ '
        '/ __| | | | '_ ` _ \| '_ \| | | |'
        '\__ \ |_| | | | | | | |_) | |_| |'
        '|___/\__, |_| |_| |_| .__/ \__, |'
        '     __/ |          | |     __/ |'
        '    |___/           |_|    |___/ '
        ##################################
    """

    src = """
    
     _       __     __    ______               __    ______      __
    | |     / /__  / /_  / ____/_______  _____/ /_  / ____/___ _/ /___  __  __
    | | /| / / _ \/ __ \/ /_  / ___/ _ \/ ___/ __ \/ /   / __ `/ / __ \/ / / /
    | |/ |/ /  __/ /_/ / __/ / /  /  __(__  ) / / / /___/ /_/ / / /_/ / /_/ /
    |__/|__/\___/_.___/_/   /_/   \___/____/_/ /_/\____/\__,_/_/ .___/\__, /
                                                              /_/    /____/
    """


    # time.sleep()
    # for again in ran
    print(src)
    # return syym

def diferentials(reguet_integral) -> str:
    x, y, z = sym.symbols('x y z')
    w , t , u = sym.symbols('w, t ,u')
    k, m , n = sym.symbols('k m n' ,integer=True)
    f, g , h = sym.symbols('f, g, h')
    oo = sym.symbols('oo')
    sym.init_printing(True)
    sensitive = "##########################################"
    complement = pprint(str(sym.Integral(reguet_integral)), use_unicode=False)
    #complement =  pprint(sym.Integral(reguet_integral), use_unicode=True)
    print(f'{sensitive}')

    for u in range(0, 1):
        time.sleep(0.2)                
        complement = pprint(sym.integrate(reguet_integral), use_unicode=True)
        with open('fixhtml/output.txt', 'w') as htf:
            htf.write('\n')
            with redirect_stdout(htf):
                complement = pprint(str(sym.Integral(reguet_integral)), use_unicode=False)
                # htf.write(print('\n'))
                complement = (print('\n'))
                complement =  pprint(sym.Integral(reguet_integral))
                complement = (print('\n'))
                complement = pprint(sym.integrate(reguet_integral), use_unicode=False)
                # rint(complement)
                # htf.write()
           
        # pprint(complement)
        #ad = sym.integrate(reguet_integral), use_unicode=True
    # how to calculte  doit() operation
    # complement code insane version out single code ignoring out sample test 
    # complement.doit()
    # how instruction resolv integrate  in  machine 

def diclivs(reguet_declivs):
    x, y, z = sym.symbols('x y z')
    w , t , u = sym.symbols('w, t ,u')
    k, m , n = sym.symbols('k m n' ,integer=True)
    f, g , h = sym.symbols('f, g, h')
    oo = sym.symbols('oo')
    sym.init_printing(True)
    reincibilization = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
    complement = pprint(str(sym.Derivative(reguet_declivs)), use_unicode=False)
    # complement =pprint(sym.Derivative(reguet_declivs), use_unicode=True)
    print(f'{reincibilization}')
    for a in range(0, 1):
        time.sleep(0.1)
        complement=pprint(sym.diff(reguet_declivs), use_unicode=True)
        with open("fixhtml/output1.txt", 'w') as  dif:
            dif.write('\n')
            with redirect_stdout(dif):
                complement = pprint(str(sym.Derivative(reguet_declivs)), use_unicode=False)
                complement =(print('\n'))
                complement = pprint(sym.diff(reguet_declivs), use_unicode=True)
        # sys.exit(0)
    # complement.doit()
def limitation(reguet_limon, reguet_val, reguet_fusse):
    x, y, z = sym.symbols('x, y, z')
    w , t , u = sym.symbols('w, t ,u')
    k, m , n = sym.symbols('k m n' ,integer=True)
    f, g , h = sym.symbols('f, g, h')
    oo = sym.symbols('oo')
    sym.init_printing(True)
    reems = "@##@#@#@#@#@#@#@#@#@#@#@#@@@#@##@##@#@#@#@#@#@"
    ument = pprint(str(sym.Limit(reguet_limon , reguet_val, reguet_fusse)), use_unicode=False)
    ument = pprint(sym.Limit(reguet_limon, reguet_val, reguet_fusse), use_unicode=True)
    print(f'{reems}')
    for s in range(0, 1):
        time.sleep(0.1)
        # ument = pprint(sym.limit(reguet_limon, reguet_val, reguet_fusse), use_unicode=True)
        with open("fixhtml/output2.txt",  'w') as limcow:
            limcow.write('\n')
            with redirect_stdout(limcow):
                ument =  pprint(str(sym.Limit(reguet_limon , reguet_val, reguet_fusse)), use_unicode=False)
                umnet = (print('\n'))
                ument = pprint(sym.Limit(reguet_limon, reguet_val, reguet_fusse), use_unicode=True)
                ument = (print('\n'))
                ument = pprint(sym.limit(reguet_limon , reguet_val, reguet_fusse), use_unicode=True)

        # sys.exit(0)
    #complement =pprint(sym.Integrate(reguet_limited), use_unicode=False)
    # complement.doit()



def cmetrix(cm_line, cm_col, cm_val):
    x , y ,z = sym.symbols('x, y ,z')
    w , t , u = sym.symbols('w, t ,u')
    k, m , n = sym.symbols('k m n' ,integer=True)
    f, g , h = sym.symbols('f, g, h')
    oo = sym.symbols('oo')
    sym.init_printing(True)
    
    cmatr = pprint(sym.Matrix([cm_val]))
    for a in range(0, 1):
        time.slepp(0.2)
        with open("fixhtml/matrix.txt", 'w') as cmati:
            cmati.write('\n')
            with redirect_stdout(cmati):
                comprex = pprint(str(sym.Matrix([str(cm_val)])), use_unicode=True)
                comprex = (print('\n'))
                # comprex = pretty_print()



def  eleven():
    x, y, z = sym.symbols('x y z')
    w , t , u = sym.symbols('w, t ,u')
    k, m , n = sym.symbols('k m n' ,integer=True)
    f, g , h, o = sym.symbols('f, g, h , o')
    oo = sym.symbols('oo')
    sym.init_printing(True)
    if  sys.argv[1] == "--mode":
        if sys.argv[2] == "--int":
            sensitive = "#############################################"
            complet = pprint(str(sym.Integral(sys.argv[3])), use_unicode=True)
            complet = pprint(sym.Integral(sys.argv[3]), use_unicode=False)
            print(f'{sensitive}')
            for u in range(0, 1):
                time.sleep(0.2)                
                complet = pprint(sym.integrate(sys.argv[3]), use_unicode=True)
            # sympy.doit()
            # sym.doit(complet)
            # print(f'#\t{complet}\t#')
            
            # pprint(complet.doit())
            sys.exit(0)
        elif sys.argv[2] == "--der":
            reincibilization = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"
            complet = pprint(str(sym.Derivative(sys.argv[3])), use_unicode=True)
            complet = pprint(sym.Derivative(sys.argv[3]), use_unicode=True)
            print(f'{reincibilization}')
            for u in range(0, 1):
                time.sleep(0.2)
                
                complet = pprint(sym.diff(sys.argv[3]), use_unicode=True )
            # complet.doit()
            sys.exit(0)
        elif sys.argv[2] == "--lim":
            reems = "@##@#@#@#@#@#@#@#@#@#@#@#@@@#@##@##@#@#@#@#@#@"
            complet = pprint(str(sym.Limit(sys.argv[3])),  use_unicode=True)
            complet = pprint(sym.Limit(sys.argv[3]),  use_unicode=False)
            
            print(f'{reems}')
        
            for z in range(0, 1 ):
                time.sleep(0.1)
                complet = pprint(sym.limit(sys.argv[3]), use_unicode=True)        
            # complet.doit()
            sys.exit(0)
        # elif  sys.argv[2] == "--lim"
    else:

        name_x=input('integral : ')
        if str(name_x):
            complt = pprint(str(sym.Integral(name_x)), use_unicode=True)
            # print('jerso3')
            complt = pprint(sym.Integral(name_x), use_unicode=True)
            print('resolving .....')
            for a in range(0, 1):
                complt = pprint(sym.integrate(name_x) , use_unicode=True)
            # complt.doit()
                sys.exit(0)
        # pprint(str(Integral(ln x, x)))
        # aprint(complt)
            #pprint(Integral(sqrt(1/x), x), use_unicode=True)


# if __name__ == '__main__':
#    for z in range(0, 1):
#        time.sleep(0.5)
#        limitation(sys.argv[1], sys.argv[2], sys.argv[3])
        # banner()
        # eleven()
