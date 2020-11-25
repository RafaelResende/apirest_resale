#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
App

Flask app
"""

import os
import sys
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

@app.route('/imobiliaria/inserir', methods=['POST'])
def inserir_imobiliaria():
    data = request.form
    if data:
        imob = Imobiliaria(data['nome'], data['endereco'])
        db_session.add(imob)
        db_session.commit()
        return "ok"


@app.route('/imobiliaria/editar', methods=['POST'])
def editarr_imobiliaria():
    data = request.form
    if data:
        imob = User.query.filter_by(username=username).all()
        db_session.add(imob)
        db_session.commit()

@app.route('/imobiliaria/deletar', methods=['DELETE'])
def deletar_imobiliaria():
    data = request.form
    if data:
        imob = Imobiliaria(data['nome'], data['endereco'])
        print (imob)
        db_session.delete(imob)
        db_session.commit()
        return "delOK"


#crud imovel

@app.route('/imovel/listar')
def listar_imovels():
    imovels = Imovel.query.all()
    imovels = [x.to_obj() for x in imovels]
    return jsonify(imovels=imovels)


@app.route('/imovel/listar/<int:imob_id>')
def listar_imovel(imob_id):
    imovel = Imovel.query.get(imob_id)
    if imovel is not None:
        return imovel.to_obj()

@app.route('/imovel/inserir', methods=['POST'])
def inserir_imovel():
    print('oi1')
    data = request.form
    print('oi2')
    if data:
        imov = Imovel(data['nome'], data['endereco'], data['descricao'], data['status'], data['caracteristica'], data['tipo'], data['finalidade'], data['imobiliaria'])
        db_session.add(imov)
        db_session.commit()
        return "ok"


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
