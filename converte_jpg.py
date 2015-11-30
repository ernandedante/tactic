#!/usr/bin/env python

# ==========================================================================================
#	 		$ Descrition - /
#
#					TACTIV DEV CONVERTER ARQUIVOS
#
#	 Converter arquivos, usando um modulo da cortex.
#	 A saida dos arquivos tem que ser de preferencia jpg, por ser uma arquivo leve.
#	 Recebe como entrada o path das imagens.
#		
#	 A conversao das imagens dessa maneira e lenta, depende do tamanho da imagem.
#
#    Tem como dependencia a cortex.
#
#	 				by:. Ernande dante
#	
#													     			 atualizacao: 30/11/2015
#
# ==========================================================================================

import os
import subprocess
from pprint import pprint

class converter():
	def __init__(self, path_arquivos):

		self.fileDiretorio = []
		self.comandos      = ["#!/bin/bash"]
		self.path_arquivos = path_arquivos

	def dirCorrent(self):

		# self.fileDiretorio.append(os.listdir('.'))
		for index, each in enumerate(os.listdir(self.path_arquivos)):
			if each[-4:] == ".tif":
				saida = each[:-3] + "jpg"
				self.comandos.append('exr2tif.py %s %s' % (each, saida))
		# print self.comandos

		# Vai escrever os comandos dos arquivos no scrpit.
		self.escrevendo(self.comandos)
		# Vai executar o script no terminal com scrpit da cortex.
		self.executando()
		self.leitura()

	def escrevendo(self, comandos):
		f = open("trigger.sh", "w")		        # (w) sobreescreve (a) anexar ao conteudo anterior
		for each in comandos:					# (r) Leitura (r+) leitura mais escrita
			f.write(each + "\n") 				# O \n faz com que cada laco, escreva em uma linha.
		f.close()

	def leitura(self):
		f = open("trigger.sh", "r")
		print f.readlines()
		f.close()

	def executando(self):
		subprocess.call("trigger.sh", shell=True)



