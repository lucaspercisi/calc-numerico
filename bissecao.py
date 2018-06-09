#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from math import *
import numpy as np

################                DADOS PARA BISSE��O             ######################

#fun��es para an�lise
def f(x):
    return 0.5*pi - asin(x) - x*np.sqrt((1-(x**2))) - 1.24 

#intervalo de an�lise (x0 deve ser menor que x1)
x0 = 0
x1 = 1

#precis�o
precicao = 10**(-5)
######################################################################################
######################################################################################

#caso seja informado um intervalo inv�lido
if(x0 >= x1):
    print ('Intervalo informado inv�lido.')
    print ('=============================================================')
    os._exit(1)

#calculo do erro relativo
def erroRel(x0, x1):
    erroAbs = abs(x1-x0)
    erroRel = abs(erroAbs/x1)
    return erroRel

#verifica a existencia da ra�z atrav�s do teorema TVI
def verificaRaiz(x0, x1):
    if(f(x0)*f(x1) < 0):
        return True
    else:
        return False

#define a quantidade de itera��es para alcan�ar a ra�z com a precis�o informada
def iteracoes(x0, x1, precicao):
    iteracoes = (log10(x1-x0) - log10(precicao)) / log10(2)
    return ceil(iteracoes-1) #retorna o teto

#algoritmo TVI
def tvi(x0, x1):
    
    if verificaRaiz(x0, x1):
        print ('DADOS PARA A BISSE��O')
        print ('Precis�o: {}'.format(precicao))
        print ('Intervalo: [{},{}]'.format(x0, x1))
        print ('Estimativa de n�mero de itera��es: {}'.format(iteracoes(x0, x1, precicao)))
        print ('Crit�rio de Parada: Erro relativo < Precis�o')
        print ('-------------------------------------------------------------')
        print ('CONVERG�NCIA')
        count_it_cont = 0
        count_it_calc = iteracoes(x0, x1, precicao)
        while erroRel(x0, x1) > precicao:
        #while count_it_calc > 0:
            xMed = ((x1-x0)/2.0) + x0#atualiza ponto m�dio

            count_it_calc -= 1
            count_it_cont += 1
            #verifica se o pr�prio ponto � a ra�z
            if(f(x0) == 0):
                print ('Quantidade de itera��es processadas: {}'.format(count_it_cont))
                print ('Ra�z no ponto x = [{}]'.format(x0))
                print ('=============================================================')
                return
            if(f(x1) == 0):
                print ('Quantidade de itera��es processadas: {}'.format(count_it_cont))
                print ('Ra�z no ponto x = [{}]'.format(x1))
                print ('=============================================================')
                return


            #verifica ra�z em um intervalo menor
            if verificaRaiz(x0, xMed):
                x1 = xMed
                print ('P{} = {}\t\tErro Relativo: {}'.format(count_it_cont, xMed, erroRel(x0, x1)))
            else:
                verificaRaiz(xMed, x1)
                x0 = xMed
                print ('P{} = {}\t\tErro Relativo: {}'.format(count_it_cont, xMed, erroRel(x0, x1)))

    else:
        print ('RESULTADOS')
        print ('Fun��o n�o possui ra�z no intervalo selecionado.')
        print ('Intervalo: [{},{}]'.format(x0, x1))
        print ('=============================================================')
        return

    #RESULTADO
    print ('-------------------------------------------------------------')
    print ('RESULTADOS')
    print ('Quantidade de itera��es processadas: {}'.format(c))
    print ('Raiz da fun��o entre os pontos x0 = {} e x1 = {})'.format(x0,x1))    
    print ('=============================================================')
    
print ('=============================================================')
print ('TRABALHO DE C�LCULO N�MERICO')
print ('Aluno: Lucas Percisi - 6� Semestre - Noturno - 28/03/2018')
print ('Teorema da Bisse��o')
print ('-------------------------------------------------------------')

tvi(x0, x1) #inicia o c�lculo
