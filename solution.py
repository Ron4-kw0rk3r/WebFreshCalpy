#!/usr/bin/python3


# from distutils.log import debug
# from crypt import methods
# from unittest import result
# from crypt import methods
#from crypt import methods
#from operator import index
#from turtle import home
import flask
from flask import Flask , render_template
from flask import request
import sys 
import math
import json
#from onjson.strucs import builder 
##import strucscode
# from strucscode 
# import strucs
import time
import sympy as sym 
from sympy import *
from sympy.abc import *
from sympy.parsing.sympy_parser import *
from brainsolver import diferentials
from brainsolver import diclivs
from brainsolver import limitation
from brainsolver import cmetrix
# how fix import text str in parser render template host in code sussesfully
# again imported code alll seeder 
import os 

# from numpy import char 




app = Flask(__name__)
@app.route('/')
def main():
    return render_template("firts_loggin.html")




@app.route('/acesspoint', methods=["POST"])
def acesspoint():
    if request.method == "POST":
        return render_template("index.html")
        # obster = request.form["Get Fresh"]



@app.route('/clubsters', methods=["POST"])
def clubsters():
    if request.method == "POST":
        charger = request.form["value_1"]
        #evaluator = str(request.form['result'])
        def buildman(operation):
            
            mmmaker =  eval(operation)
            # print(mmmaker)
            # if str(operation):
            # buildman(eval("operation"))

                # print(f'result --> {make}')
        # buildman(charger)
        # operr = buildman--(charger)
        if str(charger):
            make = eval(charger)
            print(float(make))
            return render_template("index.html", result=float(make))
        # return render_template("index.html", )
    # pass
@app.route('/strangerman', methods=["POST"])
def strangerman():
    if request.method == "POST":
        kwork = int(request.form["sq_raiz"])
        if int(kwork):
            pth = math.sqrt(kwork)          
            return render_template('index.html', ravengold=pth)




@app.route('/matrix', methods=["POST"])


def matrix():
    if request.method == "POST":
        buildcm = request.form["columna"]
        buildln = request.form["linea"]
        chcm = request.form["matrix"]
        for jok in range(0, 10):
            if jok > 2:
                note = print(f'{[jok]}', end =", ")
        if buildcm :
            return render_template("index.html", solvmatrix=chcm)



@app.route('/derivate', methods=["POST"])
def derivate():
    if request.method == "POST":
        composer = request.form["ingral_1"]
        voold =  request.form["verify"]

        aproved = diferentials(composer)
        with open("fixhtml/output1.txt", 'r') as buildman:
            
            for  exm in  buildman:
            # buildman_cont = buildman.read()
                dumpyf = exm.read()

@app.route('/limits', methods=["POST"])

def limits():
    if request.method == "POST":
        composer = request.form["limited_1"]
        limon = request.form["xam"]
        strapp = request.form["fin_xam"]
        # lomvid =  request.form["limited"]

        blimiteder = limitation(composer , limon, strapp)
        with open("fixhtml/output2.txt", 'r') as limonman:
            for  zlab in  limonman:
                lim_conf = limonman.read()


        if composer:
            return render_template("index.html", limview1=lim_conf)
            
        
            # buildman_cont = buildman.read()



@app.route('/integrals', methods=["POST"])
def integrals():
    if request.method == "POST":
        composer = request.form["ingral_1"]
        voold =  request.form["verify"]

        aproved = diferentials(composer)
        with open("fixhtml/output.txt", 'r') as buildman:
            for tm in buildman:
                buildman_cont = buildman.read()



        recreater = diclivs(composer)
        with open("fixhtml/output1.txt", "r") as mandeclif:
            for bui in mandeclif:
                derivman_conf = mandeclif.read()
            # for  exmdiclivs in  buildman:
                # dumpyf = exm.readline()
                # print(exm)
            # buildman = open("fixhtml/output.txt", 'r')
        
        # dumpyf = buildman.readline()
        # dumpyf = buildman.readline()
        # dumpyf = buildman.readline()
        # comprovating in line in text 
        # dumpyf.strip()
        # dumpfy = buildman.read()
        
        # for yum in dumpyf:
             
        # stabler = pprint(dumpyf[0:])
        # def brainsolver(example):
        #     x , y, z = sym.symbols('x, y , z')
        #     w , t , u =  sym.symbols('w, t, u')
        #     v, s, a , b = sym.symbols('v , s, a, b')

            # igral = integrate(example)
            # print(igral)
        # brainsolver(composer)
        # restap = jsonify({"solution" : buildman_cont})
        # print(aproved)
        # def brainderive(exaout):
        #     x , y, z = sym.symbols('x y z')
        #     w , t , u =  sym.symbols('w  t u')
        #     v, s, a , b = sym.symbols('v s a b')
        #      init_printing(use_unicode=True)
        #     igral = diff(exaout)
            # igral
        # new_val = brainderive(composer)

        # if int(composer):
        #     pass

        if  voold == "integral":
            return render_template('index.html', hoolview=str(buildman_cont))
            # return render_template('index.html', hoolview=dumpfy)
        elif voold == "derivate":
            return render_template('index.html', hoolview=str(derivman_conf))
       
        else:
            return render_template('error.html')

@app.route('/yettramp', methods=['POST'])
def yettramp():

    stramper = json.loads(structs)
    print(stramper['build_name'])
    # pass


@app.route('/saveme', methods=["POST"])
def saveme( assembly , declif ):
    updat_file = os.path.join('loggin.txt')
    alice = open(updat_file, 'w')
    chunck = 0
    dumping = request.form[assembly]

    for z in alice:
        chunck += 1
        z.write('#[chunck] --> dumping %H:%M:%S \n')
        # print(z)

app.run(debug=True, port=5633 ) 
if __name__ == "__main__":
    clubsters()
    strangerman()
    main()
    acesspoint()
    # pass


#https://coderslegacy.com/python/matrices-in-sympy/
# https://stackoverflow.com/questions/69554191/how-to-solve-easy-matrix-equations-thanks-to-sympy-in-python
# https://www.geeksforgeeks.org/python-sympy-matrix-method/
# https://docs.sympy.org/latest/tutorial/intro.html
