from operator import attrgetter
import math as math
import pandas as pd
#import names
from functions_and_classes import *
from random import randint


banco_alunos = pd.read_csv('python/alunos3rao.CSV')

print(banco_alunos.info() )


alunosH = banco_alunos[banco_alunos["H x M"] == "H"]
alunosM = banco_alunos[banco_alunos["H x M"] == "M"]

alunosH.sort_values(by=['Altura'], inplace=True)
alunosM.sort_values(by=['Altura'], inplace=True, ascending=False)

# print(alunosM.head(20))
# print(alunosH.head(20))


lstAlunas = []
lstAlunos = []

for index, row in alunosM.iterrows():
    lstAlunas.append(Alunos(row[1],row[0],row[2],row[4],row[3]))

for index, row in alunosH.iterrows():
    lstAlunos.append(Alunos(row[1],row[0],row[2],row[4],row[3]))
  

# print(len(lstAlunos))

# print(len(lstAlunas))

if len(lstAlunos)>len(lstAlunos):
    qtlinha = math.ceil(len(lstAlunos) /6 )
    if qtlinha % 2 != 0: 
        qtlinha+=1 
    formacaoMeninos = Formacao(lstAlunos,6,qtlinha)
    formacaoMeninos.get_posicao_alunos()
    for a in formacaoMeninos.elem :
        a.col = 7 - a.col
    formacaoMeninas = Formacao(lstAlunas,6, formacaoMeninos.nlin)
    formacaoMeninas.get_posicao_alunos()
else:
    qtlinha = math.ceil(len(lstAlunas) /6 )
    if qtlinha % 2 != 0: 
        qtlinha+=1 
    formacaoMeninas = Formacao(lstAlunas,6,qtlinha)
    formacaoMeninas.get_posicao_alunos()
    for a in formacaoMeninas.elem :
        a.col = 7 - a.col
    formacaoMeninos = Formacao(lstAlunos,6, formacaoMeninas.nlin)
    formacaoMeninos.get_posicao_alunos()

# formacaoMeninos.print_posicao_alunos()


# formacaoMeninas.print_posicao_alunos()


colunas = ['num', 'nome', 'turma', 'altura', 'sex', 'l', 'c']
arr = []

for a in formacaoMeninas.elem :
    arr.append([a.num, a.nome, a.turma, a.alt, a.sex, a.lin, a.col])

saveMeninas = pd.DataFrame(arr, columns=colunas)
saveMeninas.to_json(r'static/meninas.json', orient='records')
saveMeninas.to_csv(r'static/meninas3rao.csv',index = False)

print(saveMeninas.info())
print(saveMeninas.tail(20))

arr1 = []

for a in formacaoMeninos.elem :
    arr1.append([a.num, a.nome, a.turma, a.alt, a.sex, a.lin, a.col])


saveMeninos = pd.DataFrame(arr1, columns=colunas)

print(saveMeninos.info())
print(saveMeninos.tail(20))
saveMeninos.to_json(r'static/meninos.json', orient='records')
saveMeninos.to_csv(r'static/meninos3rao.csv', index = False)

