#!/usr/bin/env

'''
	========================================================================================
		TACTIC DEV Script Search Image * 
			Esse script tem como finalidade, busca arquivos de imagem dentro de cada pasta
			do SAM, retornando essas instrucoes em forma de uma lista e um dicionairo.

			A forma de desenvolvimento tem como base a busca dessas imagens para e seus 
			PATH.
			Com essa informa, path de cada imagem, vai ser fazer a estruturacao dos arquivos
			no banco de dados do TACTIC.

			Sera tambem	para monitorar a adicao de novos arquivos, criacao de um novo shot,
			ou Asset, a cada novo item encontrado, sera atualizado o banco de dados, como
			os novos dados.

			atualizado 17/11/2015
	========================================================================================
'''

import os
from pprint import pprint

class TacticSearch():
	def __init__(self):
		self.sam_paths 	  = { 
							'maya' : ''		,
						  	'nuke' : ''		,
						  	'houdini': '' 	
						  	}

		print "Iniciando..."

	def arvoreBusca(self):
		
		caminhoPreDefinido = "/atomo/jobs/"
		path_sam = ""
		path_render = []

		for each in os.listdir( caminhoPreDefinido ):
			path_sam = "%s%s%s" % ( caminhoPreDefinido, each, "/sam" )
			if os.path.exists( path_sam ):
				path_render.append( path_sam + "/render" )

		path_versions_maya = []
		path_versions_nuke = []
		path_versions_houdini = []

		for each in path_render:
#			Cada if seleciona os peth existente, dentro do job que tenha sido rendido com o SAM.			
			if 'maya' in os.listdir( each ):
				path_maya = each + "/maya"
				versions01 = os.listdir( path_maya )

				for i in versions01:
					path_versions_maya.append( path_maya + '/' + i )

			if 'nuke' in os.listdir( each ):
				path_nuke = each + "/nuke"
				versions02 = os.listdir( path_nuke )

				for i in versions02:
					path_versions_nuke.append( path_nuke + '/' + i )

			if 'houdini' in os.listdir( each ):
				path_houdini = each + "/houdini"
				versions03 = os.listdir( path_houdini )

				for i in versions03:
					path_versions_houdini.append( path_houdini + "/" + i )


		self.sam_paths["maya"] = path_versions_maya
		self.sam_paths["nuke"] = path_versions_nuke
		self.sam_paths["houdini"] = path_versions_houdini

# 		Retorna um dicionario com o path de cada job quem foi rendido com o SAM.
		return self.sam_paths

	def getPathFiles( self, soft ):

		nameImagens = {}
		version  = ''
		img      = ''
		pathImagens = []

# 		Listando imagens do render sonbre maya.		
		maya = self.arvoreBusca()[soft]
		for index in range( len(maya) ):
			ppath    = maya[index]
			arquivos = os.listdir( maya[index] )
			for i in arquivos:
				img = ppath + "/" + i
				try:
					imagens = os.listdir( version.join(img) )
					for j in imagens:
						img_2 = img + "/" + j
						if "images" in img_2:
# 							Todos os nomes de arquivos
							pathImagens.append( img_2 )
							nameImagens[img_2] = os.listdir( img_2 )
						else:
							pass
							# print " [%s] Not image! " % str(len(j))

				except OSError:
					pass

		return nameImagens, pathImagens, self.sam_paths


''' Essa class tem como retorno path de imagens do SAM 
	So nome de arquivos, e path de cada arquivo.
	caminho de cada sorftware, houdini, maya, nuke.

		* Todos os arquivos estao em tif ou exr             
		* Verificar como converter as imagens para jpg, ou png. '''

# m = TacticSearch()
# imagens, path, path_sam= m.getPathFiles('maya')
# print path_sam['maya']
