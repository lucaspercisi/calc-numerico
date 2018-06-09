#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import cmath
from math import *
import numpy as np

################            DADOS PARA O PONRO FIXO             ######################
######################################################################################

#funções para análise
def f(x):
    return (2*x) - (10*np.sin(x))

#derivada da função
def fi(x):
	#return (2*x/(10))/np.sqrt(1-(x**4/100))
    return np.sqrt(-10*np.cos(x))

#chute inicial
p0 = 3.0
#precisão
precisao = 10**(-4)

######################################################################################
######################################################################################

#calculo do erro relativo
def erroRel(x0, x1):
    erroAbs = abs(x1-x0)
    #erroRel = abs(erroAbs/x1)
    return erroAbs

def ponto_fixo(p0):

    print ('CONVERGÊNCIA')
    print ('-------------------------------------------------------------')
    print ('CHUTE INICIAL: {}'.format(p0))
    print ('PRECISÃO: {}'.format(precisao))
    print ('CRITÉRIO DE PARADA: ERRO R. < PRECISÃO')
    print ('\nPONTOS\t\t\t\tERRO R.\n')

    count_it_cont = 0
    print ('x{} = {}\t\t\tSOLUÇÃO INICIAL'.format(count_it_cont, p0))

    p = fi(p0)
    count_it_cont += 1
    print ('x{} = {}\t{}'.format(count_it_cont, p, erroRel(p0, p)))
 
    while(erroRel(p0, p) > precisao):
        p0 = p
        p = fi(p0)
        count_it_cont += 1
        if(count_it_cont == 1000):
        	print('Erro de loop')
        	break
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
print ('\nMétodo do Ponto Fixo')
print ('\n-------------------------------------------------------------')

ponto_fixo(p0)
