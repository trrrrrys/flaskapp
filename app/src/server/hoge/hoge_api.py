#!/usr/bin/python
# -*- coding: utf-8 -*-

# [Import start]
from flask import Blueprint, jsonify
# [Import end]

app = Blueprint(
    'hoge',
    __name__,
    url_prefix='/hoge'
)


@app.route('/test')
def hoge():
    return "\nhogehoge"
