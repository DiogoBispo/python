"""
#criar contadores do menor para o maior e
#do maior para o menor
"""

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)

"""
##gerador de cpf
"""

from random import randint
numero = str(randint(100000000, 9999999999))


novo_cpf = numero
reverso = 10
total = 0

#loop do cpf
for index in range(19):
    if index > 8:
        index -= 9
    total += int(novo_cpf[index]) * reverso

reverso -= 1
if reverso < 2:
    reverso = 11
    d = 11 - (total % 11)

    if d > 9:
        d = 0
    total = 0 
    novo_cpf += str(d)

print(novo_cpf)
