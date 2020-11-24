#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from db import Base


class Imobiliaria(Base):
    __tablename__ = 'imobiliaria'
    id = Column(Integer, primary_key=True)
    nome = Column(String(200), unique=True)
    endereco = Column(String(2000), unique=False)

    def __init__(self, nome=None, endereco=None):
        self.nome = nome
        self.endereco = endereco

    def to_obj(self):
        return {'id': self.id, 'nome': self.nome, 'endereco': self.endereco}

'''class imovel(Base):
	tablename  =  'imovel'
	id = Column(Integer, primary_key = True)
	nome = Column(String(200), unique=True)
	endereco = Column(String(2000), unique=False)
	descricao = Column(String(200), unique=False)
	status = Column(String(20), unique=False)
	caracteristica = Column(String(2000), unique=False)
	tipo = Column(String(200), unique=False)
	finalidade = Column(String(200), unique=False)
	imobiliaria = Column(String(20), unique=False)
    
	def __init__(self, nome=None, endereco=None, descricao=None, status=None, caracteristica=None, tipo=None, finalidade=None, imobiliaria=None):
		self.nome = nome
		self.endereco = endereco
		self.descricao = descricao
		self.status = status
		self.caracteristica = caracteristica
		self.tipo = tipo
		self.finalidade = finalidade
		self.imobiliaria = imobiliaria
		
	def to_obj(self):
            return {'id': self.id, 'nome': self.nome, 'endereco': self.endereco, 'descricao': self.descricao, 'status': self.status, 'caracteristica': self.caracteristica, 'tipo': self.tipo, 'finalidade': self.finalidade, 'imobiliaria': self.imobiliaria}
'''        
