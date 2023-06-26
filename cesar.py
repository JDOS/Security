import sys
import secrets
import math

caracteres = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']

def main():

    if action != '-c' or action != '-d':
        print("Ação não reconhecida!")

    if chave !='-k':    
         print("Ação não reconhecida!")

    texto = open(entrada, 'r')
    print("texto")
    print(texto)
    
    if action=='-d':
        texto_decifrado = decifrar(texto, numero)
    
    if action=='-c':
        texto_cifrado = cifrar(texto,numero)

    texto.close()

    with open('arquivo_saida','w') as f:
        f.write(textoc_ifrado)
    
    

def cifrar(texto, numero):
    texto_cifrado = ''
    for linha in texto:
        for letra in linha:
            texto_cifrado+=cifrar_caracter(letra, numero)

    return texto_cifrado

def decifrar(texto, numero):
    texto_cifrado = ''
    for linha in texto:
        for letra in linha:
            texto_cifrado+=decifrar_caracter(letra, numero)

    return texto_cifrado

def cifrar_caracter(caracter, numero):
    if caracter in caracteres:
        char_position = caracteres.index(caracter)
        total = char_position+numero
        if total >= len(caracteres):
            resto = total % len(caracteres)
            return caracteres[resto]
        else:
            return caracteres[total]
    else:
        return caracter

def decifrar_caracter(caracter, numero):
    if caracter in caracteres:
        char_position = caracteres.index(caracter)
        total = char_position-numero
        return caracteres[total]
    else:
        return caracter

def frequencia_caracter(caracter, texto):
	count = 0
	for letra in texto:
		if caracter == letra:
			count+=1
	return count

def gerar_chave(texto):
	return bin(secrets.randbits(len(texto)*2))

def vernam(texto, chave):
	texto_bits = 0b0
	print(type(texto_bits))
	for linha in texto:
		for letra in linha:
			c = bytearray(letra, 'utf-8')
			texto_bits = texto_bits<<4 | bin(ord(c))>>4
			print(bin(ord(c)))
		
	tamanho = len(texto_bits)
	print(chave)
	print("Texto em Bits")
	print(texto_bits)
	criptografia = 0xb

	for i in range(tamanho):
		if chave[i]==texto_bits[i]:
			print(bin(ord(chave[i])))
			criptografia<<1
		else:
			criptografia<<0

	print("texto Criptografado vernam")
	print(criptografia)
	cifrado = format(10, '#010b')
	print(cifrado)
	with open('vernam.rc4','w') as f:
		f.write(cifrado)
	


def toString(a):
  l=[]
  m=""
  for i in a:
    b=0
    c=0
    k=int(math.log10(i))+1
    for j in range(k):
      b=((i%10)*(2**j))   
      i=i//10
      c=c+b
    l.append(c)
  for x in l:
    m=m+chr(x)
  return m


def analise_frequencia(texto):
	total = 0
	for linha in texto:
		for letra in linha:
			if letra in caracteres:
				total+=1
	print(total)
	dic = {}
	for caracter in caracteres:
		dic[caracter]=(frequencia_caracter(caracter, texto)/total)*100

	for k,v in dic.items():
		print(k,str(v)+'%')
    
# print("CESAR")

# if len(sys.argv) <= 7:
#     print('argumentos insuficientes')
#     sys.exit()

# action = sys.argv[1]
# chave = sys.argv[2]
# numero = sys.argv[3]
# entrada = sys.argv[4]
# arquivo_entrada = sys.argv[5]
# saida = sys.argv[6]
# arquivo_saida = sys.argv[7]
# print(action)
# main()


file = open("teste.txt",  'r', encoding='utf-8')
texto = file.read()
print(texto)

print("Texto:")
analise_frequencia(texto)

numero = 17
cifrado = cifrar(texto, numero)   


print("Criptografado:")
analise_frequencia(cifrado)


file = open("teste.txt", 'r')
numero = 17
cifrado = decifrar(file, numero)   
with open('decifrado.txt','w') as f:
        f.write(cifrado)

print(cifrado)

chave = gerar_chave(texto)
vernam(texto,chave)
