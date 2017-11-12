from Student import *
from Concept import *
from ConceptGraph import *
from Question import *
import random as rand
import numpy as np

def createDummyConcept(name):
    profilingQs = []
    recQs = []
    for i in range(1, 6):
        profilingQs.append(ProfileQuestion("q" + str(i), "the question", "the answer", i-1))
        recQs.append(RecQuestion("q" + str(i), "the question", "the answer", i*0.75))

    c = Concept(name, profilingQs, recQs)

    return c

def createDummyStudent(name, conceptgraph):
    ctable = {}
    for c in conceptgraph.concepts:
        ctable[conceptgraph.concepts[c].name] = [0]*len(conceptgraph.concepts[c].profile_qs)

    s = Student(name, ctable)

    return s

# Todo
def recommendConcept():
    return

# input: concept
# output: RecQuestion with highest help_rating
def recommendQuestion(concept):
    q = max(concept.rec_qs, key=lambda item: item.help_rating)
    return q


#  simple concept map
#  c1 -> c2 -> c3
#              ^
#              |
#              c4
conceptgraph = ConceptGraph()
for i in range(1, 5):
    conceptgraph.addConcept(createDummyConcept("c" + str(i)))

conceptgraph.connectConcept(conceptgraph.concepts["c1"],conceptgraph.concepts["c2"])
conceptgraph.connectConcept(conceptgraph.concepts["c2"],conceptgraph.concepts["c3"])
conceptgraph.connectConcept(conceptgraph.concepts["c4"],conceptgraph.concepts["c3"])

students = {}
for i in range(1, 5):
    students["s" + str(i)] = createDummyStudent("s" + str(i), conceptgraph)
