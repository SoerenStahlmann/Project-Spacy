# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:02:50 2020

@author: Soeren
"""

import spacy
from spacy import displacy

"""
nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion.")

for token in doc:
    print(token.text, token.pos_, token.dep_)

print()
print("________")
print()

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
    
    
display.serve(doc, type="ent")
"""




class SpacyClassifier(object):
    
    
    def __init__(self, language_model="en_core_web_sm"):
        
        self.nlp = spacy.load(language_model)
    
    
    def classify(self, text):
        
        doc = self.nlp(text)
        
        # return svg        
        return displacy.render(doc, style="ent"), displacy.render(doc, style="dep")

        








