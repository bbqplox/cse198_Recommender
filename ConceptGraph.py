from Concept import *

class ConceptGraph(object):

    def __init__(self):
        self.concepts = {}

    def addConcept(self, c):
        self.concepts[c.name] = c

    def connectConcept(self, c1, c2):
        c1.next_concepts.append(c2)
        c2.prev_concepts.append(c1)
