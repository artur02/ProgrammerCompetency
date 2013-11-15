# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 14:43:36 2013

@author: Artur_Herczeg
"""

from flask import Flask, render_template

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

    app.debug = True
    app.run()
