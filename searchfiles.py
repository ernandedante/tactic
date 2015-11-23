#!/usr/bin/env

# ========================================================================================
# 			TACTIC DEV Script Search Image ( * Em desenvolvimento )
#  
# 	Esse script tem como finalidade, busca arquivos de imagem dentro de cada pasta
# 	do SAM, retornando essas instrucoes em forma de uma lista e um dicionairo.
#
# 	
#	A forma de desenvolvimento tem como base a busca dessas imagens para e seus 
#	PATH.
# 	Com essa informa, path de cada imagem, vai ser fazer a estruturacao dos arquivos
#  	no banco de dados do TACTIC.
#
#
# 	Sera tambem	para monitorar a adicao de novos arquivos, criacao de um novo shot,
# 	ou Asset, a cada novo item encontrado, sera atualizado o banco de dados, como
# 	os novos dados.
#	
#					by:. Ernande dante
#
# 																	atualizado 17/11/2015
# ========================================================================================

import os

class TacticSearch():
	def __init__(self):
		self.samPaths 	  = { 
							'maya'    : ''		,
						  	'nuke'    : ''		,
						  	'houdini' : '' 	
						  	}

	def arvoreBusca(self):
		
		caminhoPreDefinido = "/atomo/jobs/"
		pathSam 		   = ""
		pathRender         = []

		for each in os.listdir( caminhoPreDefinido ):
			pathSam = "%s%s%s" % ( caminhoPreDefinido, each, "/sam" )
			if os.path.exists( pathSam ):
				pathRender.append( pathSam + "/render" )

		path_versions_maya    = []
		path_versions_nuke    = []
		path_versions_houdini = []

		for each in pathRender:

#			Vai busca montar um path que tenha o caminho das imagens que
# 			estejam no sam			
			
			if 'maya' in os.listdir( each ):
				pathMaya  = each + "/maya"
				versonOne = os.listdir( pathMaya )

				for interation in versonOne:
					path_versions_maya.append( pathMaya + '/' + interation )

			if 'nuke' in os.listdir( each ):
				pathNuke  = each + "/nuke"
				versionTwo = os.listdir( pathNuke )

				for interation in versionTwo:
					path_versions_nuke.append( pathNuke + '/' + interation )

			if 'houdini' in os.listdir( each ):
				pathHoudini = each + "/houdini"
				versionThree   = os.listdir( pathHoudini )

				for interation in versionThree:
					path_versions_houdini.append( pathHoudini + "/" + interation )


		self.samPaths["maya"]    = path_versions_maya
		self.samPaths["nuke"]    = path_versions_nuke
		self.samPaths["houdini"] = path_versions_houdini

# 		Retorna um dicionario com o path de cada job quem foi rendido com o SAM.
		return self.samPaths

	def getPathFiles( self, softwareName ):

		nameImagens = {}
		version     = ''
		img         = ''
		pathImagens = []

# ~~~~~ Listando imagens do render sonbre maya.		
		maya = self.arvoreBusca()[softwareName]
		for index in range( len(maya) ):
			ppath    = maya[index]
			arquivos = os.listdir( maya[index] )
			for interation in arquivos:
				img = ppath + "/" + interation
				try:
					imagens = os.listdir( version.join(img) )
					for j in imagens:
						img_2 = img + "/" + j
						if "images" in img_2:
# ~~~~~~~~~~~~~~~~~~~~~~~~~ Todos os nomes de arquivos
							pathImagens.append( img_2 )
							nameImagens[img_2] = os.listdir( img_2 )
						else:
							pass
							# print " [%s] Not image! " % str(len(j))

				except OSError:
					pass

		return nameImagens, pathImagens, self.samPaths

# ~~~~~~~ TEST CLASS ~~~~~~~ #

m = TacticSearch()
imagens, path, pathSam = m.getPathFiles('maya')
print pathSam['maya']
