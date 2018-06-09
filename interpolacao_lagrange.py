'''
# -*- coding: utf-8 -*-
'''
import math
import numpy as np

#----------------------------------------------------------------------
#FUNC��O OPCIONAL PARA COMPARAR COM A INTERPOLA��O (OPCIONAL)
def f(x):
    return math.tan(x)

#----------------------------------------------------------------------
#LISTA DE PONTOS
'''
Pontos baseados no exercicio 6a da lista 10
(fechou com as respostas do autor)
'''
pontos_x = [0,0.25,0.50,0.75]
pontos_y = [1,1.64872,2.71828,4.48169]

#----------------------------------------------------------------------
#LEITURA MANUAL DOS DADOS (OPCINAL)
'''
#GERA Y EM FUN��O DE X (OPCIONAL)
for x in pontos_x:
    pontos_y.append(f(x))    

#INSERE PONTOS MANUALMENTE (OPCIONAL)
qtd_pontos = input("Quantidade de pontos para interpola��o: ")

for i in range(0,qtd_pontos):
    x = input("x{} = ".format(i))
    y = input("y{} = ".format(i))
    pontos_x.append(x)
    pontos_y.append(y)
    
'''

#----------------------------------------------------------------------
#GRAU M�XIMO DE INTERPOLA��O
print "POLINOMIO INTERPOLADOR DE LAGRANGE \n"
grau = input("Grau maximo de interpola��o(1 <= int <= {}): ".format(len(pontos_x)-1)) + 1
print "x: ", pontos_x
print "y: ", pontos_y

#----------------------------------------------------------------------
#PONTO DE AN�LISE
#x0 = input("Ponto de an�lise: ") #declara��o manual (opcional)
x0 = 0.43
print 'x0 = {}'.format(x0)
#----------------------------------------------------------------------
#C�LCULO DE Li
L = []
result = 1 #para o produt�rio
for i in range(0, grau): 
    print '--------'
    for j in range(0, grau):
        if (i != j):
            print x0,'-',pontos_x[j],'/',pontos_x[i],'-',pontos_x[j],'=',((x0 - pontos_x[j])/(pontos_x[i] - pontos_x[j]))
            result = result * ((x0 - pontos_x[j])/(pontos_x[i] - pontos_x[j]))
    L.append(result)
    result = 1

#----------------------------------------------------------------------
#Li * Yi
print '\nL*y'
for i in range(0, grau):
    print '--------'
    print L[i],'*',pontos_y[i],'=',L[i]*pontos_y[i]
    L[i] = L[i]*pontos_y[i]

#----------------------------------------------------------------------
#SOMAT�RIO
P = sum(L)

#--------------------------------------------------------------------------
print('\nPolinomio:')
'''
Para graus menores que o grau m�ximo
a fun��o polyfit retorna o polinomio mediano
entre todos os pontos.
'''
p  =  np.polyfit (pontos_x, pontos_y, grau-1)

casas_decimais = 5 #para os prints
j = (len(p)-1)
for i in range(0, len(p)):
    print round(p[i],casas_decimais),'x^{}'.format(j)
    j -= 1

#print 'f({}) = {}'.format(x0, round(f(x0),casas_decimais)) #caso compara��o com fun��o real (OPCIONAL)
print '\nP({}) = {}'.format(x0, round(P,casas_decimais))
#print 'Erro Abs: {}'.format(round(math.fabs(f(x0) - P),casas_decimais)) #para saber o erro abs da fun��o real (OPCIONAL)




