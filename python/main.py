from operator import attrgetter
import math as math
import pandas as pd

class Alunos:
	def __init__(self,nome,num,turma,sex,alt,lin = None,col = None): # Dados dos alunos
		self.nome = nome
		self.num = num
		self.turma = turma
		self.sex = sex
		self.alt = alt
		self.lin = lin
		self.col = col
class Formacao:
	def __init__(self, elementos, ncol, nlinhas = None): #cada formação é um objeto próprio, elem é array de Alunos, apenas colunas são necessárias
		self.elem = elem
		self.ncol = ncol
		if nlinhas is not None:
			self.nlin = nlinhas	
	def get_posicao_alunos(self): #!atribuindo coordenadas aos alunos
		k = 0      
      #!caso não tenha um número fixo de linhas      
		if self.nlin is None:
			self.nlin = math.ceil(len(self.elem)/self.ncol)
			d = float(len(self.elem)) % float(self.ncol) #d => diferença
         #caso pelotão esteja completo
         #todas as linhas são completadas da direita pra esquerda         
			if d == 0: 
					for i in range(1, self.nlin+1, 1):
						for j in range(self.ncol,0,-1):
							self.elem[k].lin= i
							self.elem[k].col = j
							k += 1         
				#caso estejam sobrando pessoas na retaguarda
				#todas as linhas até a antepenúltima são
			elif d!= 0:
				#completando todas as fileiras até a antepenúltima
				for i in range (1, self.nlin-1,  1): 
					for j in range (self.ncol, 0, -1):
						self.elem[k].lin = i 
						self.elem[k].col = j
						k += 1
						#*lidando com a penúltima linha
						# caso esteja sobrando mais do que um elemento na retaguarda:
						# 1. Começa-se posicionando eles da direita pra esquerda
						# 2. Quando apenas faltar 1 para ser posicionado, esse ficará na coluna da esquerda
					j = self.ncol #contador das colunas
					if d > 1:  #+1 elemento
						while d > 1:
							self.elem[k].lin = self.nlin -1
							self.elem[k].col = j
							k += 1
							j -= 1
							d -= 1
							self.elem[k].lin = self.nlin - 1 
							self.elem[k].col = 1
					#caso apenas um sobre na retaguarda:
					# - Este ficará na coluna da direita                     
					elif d == 1:
						self.elem[k].lin = self.nlin - 1
						self.elem[k].col = self.ncol
						k += 1         
					while j > 0:
						self.elem[k].lin = self.nlin
						self.elem[k].col = j
						j -= 1      
      #!caso tenha um número fixo de linhas      
		elif self.nlin is not None:
			#*Nº de linhas recebido seja maior do que o "correto"         
			if self.nlin > math.ceil(len(self.elem)/self.ncol):
				p = "aia"   
	def print_posicao_alunos(self):
		for k in range(len(self.elem)):
			print(self.elem[k].nome ,"L", self.elem[k].lin, ", ", "C", self.elem[k].col)
