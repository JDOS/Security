from getpass import getpass
from hashlib import sha256
import secrets
import os
from datetime import datetime

if not os.path.isfile("password.txt"): 
	print("Cadastrar")

	usuario = input("Nome de login: ")
	aux = False


	while aux == False:
		senha = sha256(getpass("Crie uma senha: ").encode('utf-8'))
		senha2 = sha256(getpass("Digite novamente a senha: ").encode('utf-8'))
		if senha.digest()!=senha2.digest():
			print("Senha inválida")
		else: 
			aux = True
	print("Usuario: "+ usuario)
	print("HASH: " + str(senha.hexdigest()))

	#salt
	salt = sha256(input("Salt do Servidor: ").encode('utf-8'))

	#salva senha e usuario
	with open('password.txt', 'w') as file:
	    file.write(usuario + " ")
	    file.write(sha256((senha.hexdigest()+salt.hexdigest()).encode('utf-8')).hexdigest())

	aux = False




	while aux == False:
		senha1 = sha256(getpass("Crie uma senha do aplicativo: ").encode('utf-8'))
		if senha1.digest()==senha.digest():
			print("Senha não pode ser igual a anterior")
		senha2 = sha256(getpass("Digite novamente a senha: ").encode('utf-8'))
		if senha1.digest()!=senha2.digest():
			print("Senha inválida")
		else: 
			aux = True
	print("HASH: " + str(senha1.hexdigest()))


	#salva senha e usuario
	with open('password.txt', 'a') as file:
	    file.write(" ")
	    file.write(senha1.hexdigest())



print("Usuario cadastrado!")

aux = False
while aux==False:
	print("LOGAR TOKEN")
	senha = sha256(getpass("senha: ").encode('utf-8'))
	#print(senha.hexdigest())
	with open('password.txt', 'r') as file:
		content = file.readlines()[0].split(" ")
		#print(content)
		usuario = content[0]
		senha_semente = content[1]
		senha_token = content[2]

	if senha.hexdigest()==senha_token:
		print("USUARIO LOGADO")
		aux=True

	else:
		print("senha incorreta")


def gerardata():
	data_e_hora_atuais = datetime.now()
	data_e_hora_em_texto = data_e_hora_atuais.strftime('%d%m%Y%H%M')
	return data_e_hora_em_texto

def gerartoken(datahora,numero):
	token = sha256((senha_semente+datahora+str(numero)).encode('utf-8'))
	return token.hexdigest()[:6]

def token(datahora):
	for i in range(0,5):
		print(gerartoken(datahora,i))


datahora = gerardata()
print("TOKENS: ")
token(datahora)

aux = False
while aux == False:
	
	if datahora != gerardata():
		print("TOKENS: ")
		datahora = gerardata()
		token(datahora)
