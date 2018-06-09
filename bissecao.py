#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from math import *
import numpy as np

################                DADOS PARA BISSEÇÃO             ######################

#funções para análise
def f(x):
    return 0.5*pi - asin(x) - x*np.sqrt((1-(x**2))) - 1.24 

#intervalo de análise (x0 deve ser menor que x1)
x0 = 0
x1 = 1

#precisão
precicao = 10**(-5)
######################################################################################
######################################################################################

#caso seja informado um intervalo inválido
if(x0 >= x1):
    print ('Intervalo informado inválido.')
    print ('=============================================================')
    os._exit(1)

#calculo do erro relativo
def erroRel(x0, x1):
    erroAbs = abs(x1-x0)
    erroRel = abs(erroAbs/x1)
    return erroRel

#verifica a existencia da raíz através do teorema TVI
def verificaRaiz(x0, x1):
    if(f(x0)*f(x1) < 0):
        return True
    else:
        return False

#define a quantidade de iterações para alcançar a raíz com a precisão informada
def iteracoes(x0, x1, precicao):
    iteracoes = (log10(x1-x0) - log10(precicao)) / log10(2)
    return ceil(iteracoes-1) #retorna o teto

#algoritmo TVI
def tvi(x0, x1):
    
    if verificaRaiz(x0, x1):
        print ('DADOS PARA A BISSEÇÃO')
        print ('Precisão: {}'.format(precicao))
        print ('Intervalo: [{},{}]'.format(x0, x1))
        print ('Estimativa de número de iterações: {}'.format(iteracoes(x0, x1, precicao)))
        print ('Critério de Parada: Erro relativo < Precisão')
        print ('-------------------------------------------------------------')
        print ('CONVERGÊNCIA')
        count_it_cont = 0
        count_it_calc = iteracoes(x0, x1, precicao)
        while erroRel(x0, x1) > precicao:
        #while count_it_calc > 0:
            xMed = ((x1-x0)/2.0) + x0#atualiza ponto médio

            count_it_calc -= 1
            count_it_cont += 1
            #verifica se o próprio ponto é a raíz
            if(f(x0) == 0):
                print ('Quantidade de iterações processadas: {}'.format(count_it_cont))
                print ('Raíz no ponto x = [{}]'.format(x0))
                print ('=============================================================')
                return
            if(f(x1) == 0):
                print ('Quantidade de iterações processadas: {}'.format(count_it_cont))
                print ('Raíz no ponto x = [{}]'.format(x1))
                print ('=============================================================')
                return


            #verifica raíz em um intervalo menor
            if verificaRaiz(x0, xMed):
                x1 = xMed
                print ('P{} = {}\t\tErro Relativo: {}'.format(count_it_cont, xMed, erroRel(x0, x1)))
            else:
                verificaRaiz(xMed, x1)
                x0 = xMed
                print ('P{} = {}\t\tErro Relativo: {}'.format(count_it_cont, xMed, erroRel(x0, x1)))

    else:
        print ('RESULTADOS')
        print ('Função não possui raíz no intervalo selecionado.')
        print ('Intervalo: [{},{}]'.format(x0, x1))
        print ('=============================================================')
        return

    #RESULTADO
    print ('-------------------------------------------------------------')
    print ('RESULTADOS')
    print ('Quantidade de iterações processadas: {}'.format(c))
    print ('Raiz da função entre os pontos x0 = {} e x1 = {})'.format(x0,x1))    
    print ('=============================================================')
    
print ('=============================================================')
print ('TRABALHO DE CÁLCULO NÚMERICO')
print ('Aluno: Lucas Percisi - 6º Semestre - Noturno - 28/03/2018')
print ('Teorema da Bisseção')
print ('-------------------------------------------------------------')

tvi(x0, x1) #inicia o cálculo
