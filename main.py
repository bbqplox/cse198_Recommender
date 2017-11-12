from Student import *
from Concept import *
from ConceptGraph import *
from Question import *
import numpy as np
import recommender as rec

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

l1 = [1, 0, 1, 0]
l2 = [0, 1, 0, 0]
l3 = [0, 1, 1, 0]

for s in students:
    students[s].updateConcept("c1", l1)
    students[s].updateConcept("c2", l2)
    students[s].updateConcept("c4", l3)

# test out stuff
# recommend concept based on number of 0s from other students and concept's neighbors
bestconcept = rec.recommendConcept(students, students["s2"], conceptgraph.concepts["c3"])
print(bestconcept)
# recommend question with highest rating
print(rec.recommendQuestion(conceptgraph.concepts[bestconcept]).help_rating)
