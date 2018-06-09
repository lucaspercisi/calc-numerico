# -*- coding: utf-8 -*-

import math
import numpy as np

#----------------------------------------------------------------------
#FUNC��O OPCIONAL PARA COMPARAR COM A INTERPOLA��O
def f(x):
    return math.tan(x)

#----------------------------------------------------------------------
#VARI�VEIS
'''
Pontos baseados no exercicio 1a da lista 11
(fechou com as respostas do autor)
'''
pontos_x = [8.1,8.3,8.6,8.7]
pontos_y = [16.94410,17.56492,18.50515,18.82091]

#LISTA PARA AS DIFEREN�AS DIVIDIDAS
DD = []
DD_temp = []

#----------------------------------------------------------------------
#LEITURA MANUAL DOS DADOS (OPCINAL)
'''
for x in pontos_x:
    pontos_y.append(f(x))    

qtd_pontos = input("Quantidade de pontos para interpola��o: ")

for i in range(0,qtd_pontos):
    x = input("x{} = ".format(i))
    y = input("y{} = ".format(i))
    pontos_x.append(x)
    pontos_y.append(y)
'''

#----------------------------------------------------------------------
#GRAU M�XIMO DE INTERPOLA��O
print "POLINOMIO INTERPOLADOR DE NEWTON \n"
grau = input("Grau maximo de interpola��o(1 <= int <= {}): ".format(len(pontos_x)-1)) + 1
print "x: ", pontos_x
print "y: ", pontos_y

#----------------------------------------------------------------------
#PONTO DE AN�LISE
#input("Ponto de an�lise: ") #entrada manual (opcional)
x0 = 8.4

#----------------------------------------------------------------------
#PRIMEIRA DIFEREN�AS DIVIDIDAS
for i in range(1, len(pontos_x)):
    DD_temp.append((pontos_y[i]-pontos_y[i-1])/(pontos_x[i]-pontos_x[i-1]))
DD.append(DD_temp[0])

#----------------------------------------------------------------------
#RESTANTE DAS DIFEREN�AS DIVIDIDAS
g = 1
j = 0
while len(DD) < grau-1:

    for i in range(1, len(DD_temp)):
        DD_temp[j] = ((DD_temp[i]-DD_temp[i-1])/(pontos_x[i+g]-pontos_x[i-1]))
        j = j + 1 

    DD.append(DD_temp[0])
    DD_temp.pop()
    g = g + 1
    j = 0

#----------------------------------------------------------------------
#PRODUT�RIO DOS TERMOS DE x
P = [] #lista de produ��es
produt = 1 #para o produt�rio

for i in range(0,len(DD)):
    for j in range(0, i+1):
        produt = produt * (x0 - pontos_x[j])
    P.append(produt)
    produt = 1
    
#----------------------------------------------------------------------
#MULTIPLICA��O PELAS DIFEREN�AS DIVIDIDAS
for i in range(0, len(DD)):
    DD[i] = DD[i] * P[i]
    
#----------------------------------------------------------------------
#ADICIONANDO f(x0)
DD.append(pontos_y[0])

#----------------------------------------------------------------------
#SOMAT�RIO
n = sum(DD)

#----------------------------------------------------------------------
print('\nPolinomio:')
'''
Para graus menores que o grau m�ximo
a fun��o polyfit retorna o polinomio mediano
entre todos os pontos.
(A FUN��O POLYFIT ESTA SENDO USADA SOMENTE PARA MOSTRAR O POLINOMIO GEN�RICO)
'''
p  =  np.polyfit (pontos_x, pontos_y, grau-1)

casas_decimais = 5 #para os prints
j = (len(p)-1)
for i in range(0, len(p)):
    print round(p[i],casas_decimais),'x^{}'.format(j)
    j -= 1

#print 'f({}) = {}'.format(x0, round(f(x0),casas_decimais)) #caso compara��o com fun��o real (OPCIONAL)
print '\nP({}) = {}'.format(x0, round(n,casas_decimais))
#print 'Erro Abs: {}'.format(round(math.fabs(f(x0) - P),casas_decimais)) #para saber o erro abs da fun��o real (OPCIONAL)

