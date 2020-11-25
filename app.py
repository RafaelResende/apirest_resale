#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
App

Flask app
"""

import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from collections import defaultdict
from db import *
from modelos import *
app = Flask(__name__)

__author__ = "Rafael Resende"
__copyright__ = "Copyright 2020"
__license__ = "Proprietary"
__version__ = "1.0.0"
__email__ = "resendern@gmail.com"


@app.route('/imobiliaria/listar')
def listar_imobiliarias():
    imobiliarias = Imobiliaria.query.all()
    imobiliarias = [x.to_obj() for x in imobiliarias]
    return jsonify(imobiliarias=imobiliarias)


@app.route('/imobiliaria/listar/<int:imob_id>')
def listar_imobiliaria(imob_id):
    imobiliaria = Imobiliaria.query.get(imob_id)
    if imobiliaria is not None:
        return imobiliaria.to_obj()
    return ""

@app.route('/imobiliaria/inserir', methods=['POST'])
def inserir_imobiliaria():
    data = request.form
    if data:
        imob = Imobiliaria(data['nome'], data['endereco'])
        db_session.add(imob)
        db_session.commit()

@app.route('/imobiliaria/selecionar', methods=['GET'])
def selecionar_imobiliaria():
    data = request.form
    if data:
        imob = User.query.filter_by(username=username).all()
        return imob

@app.route('/imobiliaria/editar', methods=['POST'])
def editarr_imobiliaria():
    data = request.form
    if data:
        imob = User.query.filter_by(username=username).all()
        db_session.add(imob)
        db_session.commit()

@app.route('/imobiliaria/deletar', methods=['POST'])
def deletar_imobiliaria():
    data = request.form
    if data:
        imob = Imobiliaria(data['nome'], data['endereco'])
        db_session.delete(imob)
        db_session.commit()

#crud imovel
@app.route('/imovel/inserir', methods=['POST'])
def inserir_imovel():
    data = request.form
    if data:
        imob = Imovel(data['nome'], data['endereco'])
        db_session.add(imob)
        db_session.commit()


@app.route('/imovel/selecionar', methods=['GET'])
def selecionar_imovel():
    data = request.form
    if data:
        imob = User.query.filter_by(username=username).all()
        return imob

@app.route('/imovel/editar', methods=['POST'])
def editarr_imovel():
    data = request.form
    if data:
        imob = User.query.filter_by(username=username).all()
        db_session.add(imob)
        db_session.commit()

@app.route('/imovel/deletar', methods=['POST'])
def deletar_imovel():
    data = request.form
    if data:
        imob = Imovel(data['nome'], data['endereco'])
        db_session.delete(imob)
        db_session.commit()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    init_db()

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
