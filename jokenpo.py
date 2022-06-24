import random
from time import sleep

user_wins = 0
computer_wins = 0
options = ['pedra', 'papel', 'tesoura']
jogar_novamente = True


while jogar_novamente:
    user_input = input('Digite Pedra/Papel/Tesoura ou Q para sair: ').lower()
    
    if user_input == 'q':
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print(f'Computador escolheu: {computer_pick}.')

    if (user_input == 'pedra') and  (computer_pick == 'tesoura'):
        print('você ganhou.')
        user_wins += 1
    elif (user_input == 'papel') and  (computer_pick == 'pedra'):
        print('você ganhou.')
        user_wins += 1
    elif (user_input == 'tesoura') and  (computer_pick == 'papel'):
        print('você ganhou.')
        user_wins += 1
    elif (user_input == 'tesoura') and  (computer_pick == 'tesoura'):
        print('Empate.')
    elif (user_input == 'papel') and  (computer_pick == 'papel'):
        print('Empate.')
    elif (user_input == 'pedra') and  (computer_pick == 'pedra'):
        print('Empate.') 
    else:
        print('Você perdeu.')
        computer_wins += 1
    
    jogar_novamente = int(input('1 para jogar novamente, 0 para não jogar mais: '))        

print(f'Você ganhou {user_wins} vezes.')
print(f'O computador ganhou {computer_wins} vezes.')
print('Goodbye')
sleep(3)

