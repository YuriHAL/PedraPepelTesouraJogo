import random

print("Jogo do Pedra,Papel,tesoura");
print('r= Pedra');
print("p= Papel");
print("s= Tesoura");
jogador = input('digite sua opcao: ');
print("sua opcao eh ",jogador);
elemento1 = input('Digite o a opcao 1: ')
elemento2 = input('Digite o a opcao 2: ')
elemento3 = input('Digite o a opcao 3: ')

lista = [elemento1, elemento2, elemento3]

computador = random.choice(lista)

print('O elemento sorteado foi:', computador)

if computador == 'r':
    if jogador == 'r':
        print("Empate entra jogador e a maquina")
    elif jogador == 'p':
        print("Papel embola pedra\\ Jogador VENCEU")
    elif jogador == 's':
        print('Pedra quebra tesoura\\ Computador Venceu')    
elif computador == 'p':
    if jogador == 'p':
        print("Empate entra jogador e a maquina")
    elif jogador == 'r':
        print("papel embola pedra\\ COMPUTADOR VENCEU")
    elif jogador == 's':
        print('Tesoura corta papel\\ Jogador Venceu')  
elif computador == 's':
    if jogador == 'p':
        print("Eetsoura corta papel\\Computador venceu")
    elif jogador == 'r':
        print('pedra quebra tesoura\\JOGADOR VENCEU')
    elif jogador == 's':
        print('Empate')            
