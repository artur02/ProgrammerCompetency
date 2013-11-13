# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 14:43:36 2013

@author: Artur_Herczeg
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', name="AAA")
#    return """<!doctype html>
#<html ng-app>
#  <head>
#    <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.2.0/angular.min.js"></script>
#  </head>
#  <body>
#    <div>
#      <label>Name:</label>
#      <input type="text" ng-model="yourName" placeholder="Enter a name here">
#      <hr>
#      <h1>Hello {{yourName}}!</h1>
#    </div>
#  </body>
#</html>"""

if __name__ == "__main__":
    app.debug = True
    app.run()
