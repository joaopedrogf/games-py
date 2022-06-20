print('Bem-vindo, jogador.')

playing = input('Quer jogar? ')

if playing.lower() != 'sim':
    quit()

answer = input('Qual é a melhor linguagem de programação? R:')
#Questão 1
if answer.lower() == 'python':
    print('Boa!!!')
    acertos = 1
else:
    print('Errado.')
#Questão 2
answer = input('Em que ano começou a primeira guerra mundial? R:')

if answer == '1914':
    print('Boa!!!')
    acertos += 1
else:
    print('Errado.')
#Questão 3
answer = input('Qual foi a primeira seleção a conquistar uma copa do mundo? R:')

if answer.lower() == 'uruguai':
    print('Boa!!!')
    acertos += 1
else:
    print('Errado.')
#Questão 4
answer = input('Qual a melhor pizzaria da cidade de Santos? R:')

if answer.lower() == 'big pizzas':
    print('Boa!!!')
    acertos += 1
else:
    print('Errado.')

print(f'Sua pontuação foi de:{acertos}')
print(f'Aproveitamento de :{(acertos/4)*100}%.')