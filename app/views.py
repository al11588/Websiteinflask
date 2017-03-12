#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alvin Lawson
# @Date:   2015-05-11 12:40:10
# @Last Modified by:   Alvin Lawson
# @Last Modified time: 2015-05-11 13:12:49
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")
