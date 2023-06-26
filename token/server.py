from getpass import getpass
from hashlib import sha256
import secrets
import os
from datetime import datetime
import random


def cadastrar():
	if not os.path.isfile("server.txt"): 
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
		salt = random.randint(1000,9999)
		print("Utilize o Número para o cadastro no TOKEN: ")
		print(salt)

		#salva senha e usuario
		with open('server.txt', 'w') as file:
		    file.write(usuario + " ")
		    file.write(senha.hexdigest()+ " ")
		    file.write(sha256(str(salt).encode('utf-8')).hexdigest())

	print("Usuario cadastrado!")



def gerardata():
	data_e_hora_atuais = datetime.now()
	data_e_hora_em_texto = data_e_hora_atuais.strftime('%d%m%Y%H%M')
	return data_e_hora_em_texto

def gerartoken(datahora,numero):
	with open('server.txt', 'r') as file:
		content = file.readlines()[0].split(" ")
		senha_semente = content[1]
		salt = content[2]

	senha_salt = sha256((senha_semente+salt).encode("utf-8")).hexdigest()

	token = sha256((senha_salt+datahora+str(numero)).encode('utf-8'))
	return token.hexdigest()[:6]

def token(datahora):
	tokens =[]
	for i in range(0,5):
		tokens.append(gerartoken(datahora,i))
		print(tokens)
	return tokens


def logar():
	aux = False
	while aux==False:
		print("LOGAR TOKEN")
		user = input("Nome de login: ")
		senha_token = getpass("senha token: ")
		#print(senha.hexdigest())
		with open('server.txt', 'r') as file:
			content = file.readlines()[0].split(" ")
			#print(content)
			usuario = content[0]
			senha_semente = content[1]
			salt = content[2]

		datahora = gerardata()
		if usuario == user:
			if senha_token in token(datahora):
				print("USUARIO LOGADO")
				aux = True
		else:
			print("senha incorreta")





def Main():
	aux = False
	print("SERVER")
	print("1) Cadastrar")
	print("2) LOGAR")
	print("")
	while aux == False:
		opcao = input("Escolha uma opção: ")
		if opcao == "1":
			return cadastrar()
		if opcao == "2":
			return logar()


Main()