#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from math import *

################                DADOS PARA NEWTON               ######################
######################################################################################

#funções para análise
def f(x):
	return (1/2)+((1/4)*(x**2) - x*sin(x) - (1/2)*cos(2*x))
    #return (10*(x**3)) - (8.3*(x**2)) + (2.295*x) - 0.21141

#derivada da função
def derivada_f(x):
    #return (30*(x**2)) - (16.6*(x)) + 2.295
    return x/2 - sin(x) + sin(2*x) + x* (-cos(x))

#chute inicial
p0 =  5*pi

#precisão
precisao = 10**(-3)

######################################################################################
######################################################################################

#calculo do erro relativo
def erroRel(x0, x1):
    erroAbs = abs(x1-x0)
    erroRel = abs(erroAbs/x1)
    return erroRel

def newton(p0):

    if(derivada_f(p0) == 0):
        print('Escolha outro chute inicial.')
        return

    if(f(p0) == 0):
        print('Raíz em x = {}'. format(p0))
        return


    print ('CONVERGÊNCIA')
    print ('-------------------------------------------------------------')
    print ('CHUTE INICIAL: {}'.format(p0))
    print ('PRECISÃO: {}'.format(precisao))
    print ('CRITÉRIO DE PARADA: ERRO R. < PRECISÃO')
    print ('\nPONTOS\t\t\tERRO R.\n')

    count_it_cont = 0
    print ('x{} = {}\t\tSOLUÇÃO INICIAL'.format(count_it_cont, p0))

    p = p0-(f(p0)/derivada_f(p0))
    count_it_cont += 1
    print ('x{} = {}\t{}'.format(count_it_cont, p, erroRel(p0, p)))

    while(erroRel(p0, p) > precisao):
        p0 = p
        p = p0-(f(p0)/derivada_f(p0))
        count_it_cont += 1
        print ('x{} = {}\t{}'.format(count_it_cont, p, erroRel(p0, p)))

    #RESULTADO
    print ('\n-------------------------------------------------------------')
    print ('RESULTADOS')
    print ('x{} =\t\t{}'.format(count_it_cont, p))
    print ('f(x{}) =\t\t{}'.format(count_it_cont, f(p)))
    print ('Erro R. =\t{}'.format(erroRel(p0, p)))
    print ('=============================================================')

    
print ('=============================================================')
print ('TRABALHO DE CÁLCULO NÚMERICO')
print ('Aluno: Lucas Percisi - 6º Semestre - Noturno - 15/04/2018')
print ('\nMétodo de Newton ')
print ('\n-------------------------------------------------------------')

newton(p0)
