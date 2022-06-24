#!/usr/bin/python
# *-* coding:utf-8 *-*

# creator subinstance in matrix script secuence opertors 

from sympy import *
import sympy as stm
from sys import stdin 
from sympy.abc import *
import sys




# how to create matrix values 

class makeval:
    x ,y,z = stm.symbols('x, y, z')

    def __init__(self, numbers, process):
        global x,y,z
        self.numbers = numbers
        # self.chractrs = 
        self.process = process
    def subinstance(self):
        #pass
        # self.chractrs = a, b, c
        self.uspper = [ z for z in range(0, self.numbers)]
        print(self.uspper)
    
    def  matxx(self, op3ration) -> str:
        global x,y,z
        init_printing(True)
        for acrostig in range(0, 1):
            self.nmaslow = pretty_print(stm.Matrix([[op3ration, op3ration], [2, 4]]))
            # matrix
            print('#########################')
            # print(self.nmaslow)
        # print([ x for x in range(0, numbers) ])
        
joberr = makeval(11, 10)
joberr.subinstance()
joberr.matxx('xy')
# print(joberr)



def onematrix(values) -> None:
    x, y ,z = stm.symbols('x,y,z')
    # init_printing(True)
    # for a in range(0, 1):
    #now = pretty_print(stm.Matrix([[1, 2]]))
    pprint(stm.Matrix([values, 1, 1]))
        #print(stm.Matrix([values]))
    

def matxx(operation) -> int:
    x, y ,z = stm.symbols('x, y, z')
    init_printing(True)
    for cros in range(0, 1):
        colpser = [ f for f in range(0, operation)]
        modshet = pretty_print(stm.Matrix([colpser, colpser ]))
        # nowless = pretty_print(stm.Matrix([[operation,operation], [2,2]]))
        
        # jobeer = 
    
if __name__ == "__main__":
    # matxx(sys.argv[1])
    # onematrix(sys.argv[1])

