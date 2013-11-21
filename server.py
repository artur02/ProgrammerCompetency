# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 14:43:36 2013

@author: Artur_Herczeg
"""
import os
import sys


def fix_path():
    # credit:  Nick Johnson of Google
    sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

fix_path()

from flask import Flask, render_template, url_for

import database as db
from domain import Capability


app = Flask(__name__)

Session = db.createSessionClass()
db.initDB(Session)


@app.route("/")
def index():
    session = Session()

    allcap = session.query(Capability)
    categories = session.query(Capability.category).distinct()

    processed = list()
    for cat in categories:
        subcats = session.query(Capability.subcategory).distinct()

        for sub in subcats:
            items = session.query(
                Capability.level, Capability.description).filter(
                Capability.category == cat, Capability.subcategory == sub)
            processed.append((cat, sub, items))

    return render_template(
        'index.html',
        categories=categories, items=allcap)

if __name__ == "__main__":
    with app.test_request_context():
        url_for('static', filename='style.css')
        url_for('static', filename='jquery.floatThead.min.js')
        url_for('static', filename='processor.js')

    app.debug = True
    app.run()
