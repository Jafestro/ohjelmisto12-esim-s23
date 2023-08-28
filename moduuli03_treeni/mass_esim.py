# Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä,
# nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa
# tuloksen käyttäjälle.

# Yksi leiviskä on 20 naulaa.
# Yksi naula on 32 luotia.
# Yksi luoti on 13,3 grammaa.
'''
Jotta saisit laskettua, joudut ensin selvittämään:
kuinka monta naulaa leiviskä on
kuinka monta luotia naulat on
nyt sinulla on läjä nauloja
'''

leiviskät = int(input('Anna leiviskät: '))
naulat = int(input('Anna naulat: '))
luodit = int(input('Anna luodit: '))


naulatYht = naulat + 20 * leiviskät

luoditYht = luodit + naulatYht * 32

yht = luoditYht * 13.3
print(f'Grammoja yheensä: {yht}')

# nyt grammat pitäisi saada muunnettua kiloiksi ja grammoiksi
kilot = int(yht // 1000)
gramma = yht % 1000

print('Massa nykymittojen mukaan:')
print(f'{kilot} kilogrammaa ja {gramma:.2f} grammaa')

