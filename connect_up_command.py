#!/usr/bin/env python

# ==========================================================================================
#	 		$ Descrition - /
#
#					TACTIV DEV SCRIP CONNECT TO server
#
#	 Faz a ligacao com o servidor. Ira manda os arquivos que foram selecionados.
#
#	 				by:. Ernande dante
#	
#													     			 atualizacao: 23/11/2015
#
# ==========================================================================================

# import apenas para teste, jeito tosto

from searchfiles import TacticSearch
from converte_jpg import converter
import os, sys

# ------------------------------------------------------------------------------------------
# import apenas para teste, jeito tosto

ppath = 'xxx'

if os.path.exists( ppath ):
	
	print ( 'Path exist!' )
	
	sys.path.append( 'xxx' )
	
	try:

		from tactic_client_lib import TacticServerStub, TacticApiException
		
		server = TacticServerStub()
		
		print ('Importado com sucesso! *** ')

	except ImportError:
		
		print ('Modulo nao foi encontrado.')

# ------------------------------------------------------------------------------------------

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

''' Toda parte de configuracao de servidor '''

		projeto_name = 'xxxx'
		ip_sever     = 'xxx.xxx.x.xx'

		if projeto_name:
			server = TacticServerStub()
			server.set_server(ip_sever)
			server.set_project(projeto_name)
			print 'OK server'
		else:
			print 'server down'

		search_type = projeto_name + '/shot'
		print 'USER LOGIN: %s' % (server.get_login())
		print server.build_search_type(search_type)

''' Inicializando a busca por arquvos '''

		# self.nameSnapshots()

	def converter_jpg(self, path):
		# Vai converter todas as imagens que forem necessarias.
		converter(path)

	def nameSnapshots(self):
		for index, itens in enumerate(self.paths):
			# Code recebe o nome que vai ser colocado no snapshot.
			self.listNameSnapshots.append({ 'code': '', 'description' : itens })	
			if os.listdir(itens):
				for i in os.listdir(itens):
					# Atualiza o valor da lista com para seta cada nome de arquivos com seu path
					self.listNameSnapshots[index].update(code=i[:-4])
		return self.listNameSnapshots	


	# def verificar(self):
	# 	if self.listNameSnapshots:
	# 		for i in range(len(self.listNameSnapshots)):
	# 			if server.get_by_code(search_type, self.nameSnapshots()[i]['code']):
	# 				code_triagem = server.get_by_code(search_type, self.nameSnapshots()[i]['code'])
	# 				if code_triagem['code']:
	# 					print str(self.nameSnapshots()[i]['code']) + "codigos"
	# 				else:
	# 					return True


	def creatSnapshot(self):
		''' Essa funcao deve criar os snapshot, que vao receber arquivos.
			Para cada aquivo que for updado, teve se ter um snapshot, por
			tanto ela vai ser usada em loop.'''

		# self.nameSnapshots() # inicializa a nomeacao dos snapshot
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
# print c.go()


