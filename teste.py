print("A senha deve ter pela menos um caracter Maisculo")
print("A senha un número")
senha = str(input("senha :"))


while senha.islower():
    senha = input("A senha deve ter pelo menos uma letra Maiuscula ")

while len(senha) < 7:
    senha = input("A senha ter pelo menos 8 caracteres")
