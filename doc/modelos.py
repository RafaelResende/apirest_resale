#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from db import Base


class Imobiliaria(Base):
    __tablename__ = 'imobiliaria'
    id = Column(Integer, primary_key=True)
    imovel = relationship("Imovel")
    nome = Column(String(200), nullable=False)
    endereco = Column(String(200))


    def __init__(self, nome=None, endereco=None):
        self.nome = nome
        self.endereco = endereco

    def to_obj(self):
        return {'id': self.id, 'nome': self.nome, 'endereco': self.endereco}


class Imovel(Base):
	__tablename__  =  'imovel'
	id = Column(Integer, primary_key = True)
	id_imobiliaria = Column(Integer, ForeignKey('imobiliaria.id'))
	nome = Column(String(200), unique=True, nullable=False)
	endereco = Column(String(200), nullable=False)
	descricao = Column(String(200), nullable=False)
	status = Column(String("Ativo", "Inativo"), nullable=False)
	caracteristica = Column(String(2000))
	tipo = Column(String("Apartamento", "Casa"), nullable=False)
	finalidade = Column(String("Residencial", "Escrit'orio"))
	imobiliaria = Column(String(20),nullable=False)

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
