# Você foi contratado para desenvolver um sistema de verificação de acesso a um website. O sistema deve solicitar ao usuário que insira seu nome de usuário e senha. Além disso, o sistema deve verificar se o usuário é um administrador ou um usuário comum.
# Escreva um programa em Python que implemente essa funcionalidade utilizando as estruturas if, else, and e or. As condições para verificar o acesso são as seguintes:
# 1 - Se o nome de usuário for "admin" e a senha for "admin123", o programa deve imprimir a mensagem: "Bem-vindo, administrador!".
# 2 - Se o nome de usuário for qualquer outro e a senha for "senha123", o programa deve imprimir a mensagem: "Bem-vindo, usuário comum!".
# 3 - Se o nome de usuário for "admin" mas a senha não for "admin123", o programa deve imprimir a mensagem: "Senha incorreta para o administrador.".
# 4 - Se o nome de usuário for diferente de "admin" e a senha não for "senha123", o programa deve imprimir a mensagem: "Combinação de nome de usuário e senha inválida."

print("Faça login na sua conta.")
nome = input("Nome de usuario: ")
senha = input("Digite sua senha: ")
if ( nome == "admin" and senha == "admin123" ):
    print("Bem-vindo, administrador")
elif ( nome != "admin" and senha == "senha123"):
    print("Bem-vindo, usuario comum.")   
elif ( nome == "admin" and senha != "admin123"):
    print ("Senha incorreta para o administrador.")
else:
    print("combinação de nome e senha incorretas")    