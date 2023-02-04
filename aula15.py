"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')

"""
Execute uma ação enquanto a condição for verdadeira
"""

contador = 0
while contador <= 100:
    contador = contador + 1
    print(contador)
