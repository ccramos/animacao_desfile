from operator import attrgetter
import math as math
import pandas as pd
#import names
from random import randint

#### !!!! CRIANDO AS CLASSES DE ALUNO E DE FORMAÇÃO !!!! ####

class Alunos:
	def __init__(self,nome,num,turma,sex,alt,lin = None,col = None): # Dados dos alunos
		self.nome = nome
		self.num = num
		self.turma = turma
		self.sex = sex
		self.alt = alt
		self.lin = lin
		self.col = col

		def __str__(self): #!função para imprimir o objeto
			if self.lin == None and self.col == None:
				return '\nNome: ' + self.nome + '\nNúmero: ' + self.num + '\nTurma: ' + self.turma + '\nAltura: ' + self.alt
			elif self.lin == None and self.col != None:
				return '\nNome: ' + self.nome + '\nNúmero: ' + self.num + '\nTurma: ' + self.turma + '\nAltura: ' + self.alt + '\nColuna: ' + self.col
			elif self.lin != None and self.col == None:
				return '\nNome: ' + self.nome + '\nNúmero: ' + self.num + '\nTurma: ' + self.turma + '\nAltura: ' + self.alt + '\nLinha: ' + self.lin
			elif self.lin != None and self.col != None:
				return '\nNome: ' + self.nome + '\nNúmero: ' + self.num + '\nTurma: ' + self.turma + '\nAltura: ' + self.alt + '\nLinha: ' + self.lin + '\n Coluna'
class Formacao:
	def __init__(self, elem, ncol, nlinhas = None): #cada formação é um objeto próprio, elem é array de Alunos, apenas colunas são necessárias
		self.elem = elem
		self.ncol = ncol
		self.nlin = nlinhas
				
	def get_posicao_alunos(self): #!atribuindo coordenadas aos alunos
		k = 0
		
		#!caso não tenha um nº fixo de linhas ou nº fixo seja igual ao nº necessário
		
		if self.nlin is None or self.nlin == math.ceil(len(self.elem)/self.ncol):
			self.nlin = math.ceil(len(self.elem)/self.ncol)
			d = float(len(self.elem)) % float(self.ncol) #d => diferença
			
			
			#*caso pelotão esteja completo (d = 0)
			#*todas as linhas são completadas da direita pra esquerda
			
			if d == 0: 
				for i in range(1, self.nlin+1, 1):
					for j in range(self.ncol,0,-1):
						self.elem[k].lin= i
						self.elem[k].col = j
						k += 1
			
			#*caso estejam sobrando pessoas na retaguarda
			#*todas as linhas até a antepenúltima são completas
			#*penúltima linha tratada especialmente
			#*última linha (retaguarda) completa
			
			elif d!= 0: 
				
				#*completando todas as fileiras até a antepenúltima
				
				for i in range (1, self.nlin-1,  1): 
					for j in range (self.ncol, 0, -1):
						self.elem[k].lin = i 
						self.elem[k].col = j
						k += 1
				
				#*lidando com a penúltima linha
			
				#? caso esteja sobrando mais do que um elemento na retaguarda:
				#* 1. Começa-se posicionando eles da direita pra esquerda
				#* 2. Quando apenas faltar 1 para ser posicionado, esse ficará na coluna da esquerda
				
				j = self.ncol #contador das colunas
				
				if d > 1:  #+1 elemento
					while d > 1:
						self.elem[k].lin = self.nlin -1
						self.elem[k].col = j
						k += 1
						j -= 1
						d -= 1
					
					j = 1
					self.elem[k].lin = self.nlin -1
					self.elem[k].col = 1
					k += 1

				#* caso apenas um sobre na retaguarda:
				#* - Este ficará na coluna da direita
							
				elif d == 1:
					self.elem[k].lin = self.nlin - 1
					self.elem[k].col = self.ncol
					k += 1
			
				for j in range (self.ncol, 0, -1):
					self.elem[k].lin = self.nlin
					self.elem[k].col = j
					k += 1
		
		#!caso tenha um número fixo de linhas
		
		elif self.nlin != math.ceil(len(self.elem)/self.ncol):
			

		#? ****** Nº de linhas recebido é maior do que o mínimo******
			if self.nlin > math.ceil(len(self.elem)/self.ncol):

				e = len(self.elem) #*n de elementos na formação
				Af = self.ncol * self.nlin #* área da nova formação
				ei = self.ncol - 2 #* número de elementos "internos" a cada fileira
				bur = Af - e #*tamanho do "buraco" na formação
				lin_2el = []
				lin_semi = []
				k = 0

				for i in range (self.nlin-1, 1, -1): #? determinando quantos elementos por cada linha
					if bur >= ei:
						lin_2el.append(i)
						bur -= ei
					elif bur < ei and bur != 0:
						lin_semi = [i,bur]
						break

				#! caso não haja uma linha incompleta e com mais de duas pessoas

				if len(lin_semi) != 2:
					for i in range (1,lin_2el[len(lin_2el)-1],1): #? preencher as linhas completas
						for j in range(self.ncol, 0, -1):
							self.elem[k].lin = i
							self.elem[k].col = j
							k += 1
				
				#! caso haja uma linha incompleta e outras com 2 pessoas

				elif len(lin_semi) == 2:
					
					for i in range (1,lin_semi[0],1): #? preencher as linhas completas
						for j in range(self.ncol, 0, -1):
							self.elem[k].lin = i
							self.elem[k].col = j
							k += 1

					j = self.ncol #contador das colunas
					d = self.ncol - lin_semi[1]
					if d > 1:  #+1 elemento
						while d > 1:
							self.elem[k].lin = lin_semi[0]
							self.elem[k].col = j
							k += 1
							j -= 1
							d -= 1
						
						j = 1
						self.elem[k].lin = lin_semi[0]
						self.elem[k].col = 1
						k += 1

					elif d == 1:
						self.elem[k].lin = lin_semi[0]
						self.elem[k].col = self.ncol
						k += 1

					
				for i in range(lin_2el[len(lin_2el)-1],self.nlin,1): #? preencher linhas com 2 elementos
					for j in range(2):
						self.elem[k].lin = i
						if j == 0:
							self.elem[k].col = self.ncol
						elif j == 1:
							self.elem[k].col = 1
						k += 1

				for j in range(self.ncol, 0, -1): #?preencher a retaguarda
					self.elem[k].lin = self.nlin
					self.elem[k].col = j
					k += 1


			elif self.nlin < math.ceil(len(self.elem)/self.ncol): #? nº de linhas recebido < mínimo
				return 'Impossível: não há fileiras o suficiente para completar a formação'


	#imprimir dados de Nome e posição dos alunos
					
	def print_posicao_alunos(self):
		for k in range(len(self.elem)):
			print(self.elem[k].nome ,"L", self.elem[k].lin, ", ", "C", self.elem[k].col)
def teste_formacao(caso): # Teste para sistema de formações

	#****Gerando alunos****

	quantidade = randint(40,40)

	nomes = []
	for i in range (quantidade):
		nomes.append(names.get_full_name())

	alturas = []
	for i in range (quantidade):
		alturas.append(str(randint(160,190)))

	numeros = []
	for i in range (quantidade):
		numeros.append(str(randint(1,30)))

	turmas_possiveis = ('A','B','C','D','E','F','G','H')
	turma = []
	for i in range (quantidade):
		turma.append(turmas_possiveis[randint(0,len(turmas_possiveis)-1)])

	sexos = ('M','F')
	sexo = []
	for i in range (quantidade):
		sexo.append(sexos[randint(0,len(sexos)-1)])

	elem = []
	for i in range (quantidade):
		elem.append(Alunos(nomes[i], numeros[i], turma[i], sexo[i], alturas[i]))


		#* Testando todos os casos


	if caso == 1: # pelotão cheio
		forma = Formacao(elem,4)
		forma.get_posicao_alunos()
		forma.print_posicao_alunos()
	
	if caso == 2: # formar retaguarda
		forma = Formacao(elem,6)
		forma.get_posicao_alunos()
		forma.print_posicao_alunos()
	
	if caso == 3: #numero de linhas maior do que o certo, pelotão cheio
		forma = Formacao(elem,4,12)
		forma.get_posicao_alunos()
		forma.print_posicao_alunos()

	if caso == 4: #numero de linhas maior que o certo, pelotão com retaguarda
		forma = Formacao(elem,6,11)
		forma.get_posicao_alunos()
		forma.print_posicao_alunos() 

	if caso == 5: #numero de linhas insuficiente
		forma = Formacao(elem,6,5)
		forma.get_posicao_alunos()
		forma.print_posicao_alunos() 

#### !!!! IMPORTING FROM EXCEL USING PANDAS !!!! ####
		
