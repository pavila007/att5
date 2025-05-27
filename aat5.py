import statistics
#Lista com 14 números em ordem crescente 
dados = [10, 12, 15, 18, 20, 22, 25, 28, 30, 32, 35, 38, 40, 45]
#Cálculo da média 
media = statistics.mean (dados)

#Calculo da mediana
mediana = statistics.median (dados)
print ("Média:", media)
print ("Mediana:", mediana)

from statistics import mean, median

media = mean (dados)
mediana = median (dados)

print ("Média (import total):", media)
print ("Média (import total):", mediana)

from statistics import *

media = mean (dados)
mediana = median (dados)

print ("Média (import total):", media)
print ("Mediana (import total);", mediana)
