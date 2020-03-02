# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:31:33 2020

@author: Soeren
"""

from flask import Flask, Markup
from flask import render_template, request
from spacy_app import SpacyClassifier

app = Flask(__name__)

classifier = SpacyClassifier()

@app.route("/", methods=["GET", "POST"])
def index():
    
    
    if (request.method == 'POST'):
        
        
        ents, deps = classifier.classify(request.form['exampleMessage'])
        
        #app.logger.info(entities)
        
        return render_template("index.html", ent=Markup(ents), dep=Markup(deps))
        
        
    
    if (request.method == 'GET'):
    
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000)

