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

__author__ = "Rafael Rezende"
__copyright__ = "Copyright 2020"
__license__ = "Proprietary"
__version__ = "1.0.0"
__email__ = "rafaelrezende@gmail.com"


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


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    init_db()

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
