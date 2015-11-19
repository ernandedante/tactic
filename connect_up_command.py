#!/usr/bin/env python

'''
	========================================================================================
		TACTIC DEV Script Connect to server * 
			Faz a criacao dos snapshot no trabalho que for setado. 
			Os nomes do snapshot vao ser nomeados com o nome do proprio render. Assim se 
			cria um snapsho com uma identidade unica.

			atulizado : 17/11/2015
	========================================================================================
'''

from searchfiles import TacticSearch
from pprint import pprint
import os

''' Essa classe por enquanto apenas mostra algumas etapas para upar um arquivo.
	Ela recebe um dicionario com varios caminhos, nos quais ja foram selecionados
	arquivos da pasta do SAM.
'''

class ConnectionTactic():
	def __init__(self):
		self.listNameSnapshots = []
		# Inicializando a classe que vare todo o servidor buscando caminhos de 
		# imagens do SAM. 
		self.imagens, self.paths, self.paths01 = TacticSearch().getPathFiles("maya")
		# self.search_type = 'atomo'
		self.search_type = 'atomo/shot'

	def nameSnapshots(self):
		# nameSnap = "NOMEFIGURA_"
		for index, itens in enumerate(self.paths):
			# Code recebe o nome que vai ser colocado no snapshot.
			self.listNameSnapshots.append({ 'code': '', 'description' : itens })	
			if os.listdir(itens):
				for i in os.listdir(itens):
					self.listNameSnapshots[index].update(code=i)
		return self.listNameSnapshots	

	def verificar(self):
		for i in range(len(self.listNameSnapshots)):
			if server.get_by_code(search_type, self.nameSnapshots()[i]['code'])
				code_triagem = server.get_by_code(search_type, self.nameSnapshots()[i]['code'])
				if code_triagem['code']:
					print str(self.nameSnapshots()[i]['code']) + "codigos"
				else:
					return True

	def creatSnapshot(self):
		''' Essa funcao deve criar os snapshot, que vao receber arquivos.
			Para cada aquivo que for updado, teve se ter um snapshot, por
			tanto ela vai ser usada em loop.'''
		# 
		self.nameSnapshots()
		for index in range(len(self.listNameSnapshots)):
			result = server.insert(self.search_type, self.listNameSnapshots[index])
			print "-- loop %s " % result 

	def updateSnapshot(self):
		''' Essa funcao vai fazer o upload dos arquivos'''
		for i in range(len(self.listNameSnapshots)):
			code = nameSnapshots()[i]['code']
			search_key = server.build_search_key(self.search_type, code)
			snapshot_code = server.create_snapshot(search_key, 'model')
			server.add_file(snapshot_code.get('code'), self.nameSnapshots + '/' + code, mode='upload', create_icon=True)

c = ConnectionTactic()
print c.creatSnapshot()


