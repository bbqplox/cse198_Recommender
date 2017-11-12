from Student import *
from Concept import *
from ConceptGraph import *
from Question import *
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

# input: all students, the struggling student, the concept wrong
# output: best concept for that student to review
def recommendConcept(students, stu, cwrong):
    matched = gatherConceptTables(students, stu, cwrong)

    conceptsToConsider = [c.name for c in cwrong.prev_concepts]
    conceptsToConsider = conceptsToConsider + [cwrong.name]

    zeroCounts = [zeroCounter(m, conceptsToConsider) for m in matched]

    zeroCounts = np.array(zeroCounts)
    zeroCounts = zeroCounts.T

    means = [np.mean(z) for z in zeroCounts]

    ind = means.index(max(means))

    return conceptsToConsider[ind]

def gatherConceptTables(students, stu, cwrong):
    matched = [students[s].concept_table for s in students if students[s].concept_table[cwrong.name] == stu.concept_table[cwrong.name] and students[s] is not stu]

    return matched

def zeroCounter(m, considered):

    zeroCounts = []

    for c in considered:
        zeroCounts.append(m[c].count(0))

    return zeroCounts



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

l1 = [1, 0, 1, 0]
l2 = [0, 1, 0, 0]
l3 = [0, 1, 1, 0]

for s in students:
    students[s].updateConcept("c1", l1)
    students[s].updateConcept("c2", l2)
    students[s].updateConcept("c4", l3)

# test out stuff
# recommend concept based on number of 0s from other students and concept's neighbors
bestconcept = recommendConcept(students, students["s2"], conceptgraph.concepts["c3"])
print(bestconcept)
# recommend question with highest rating
print(recommendQuestion(conceptgraph.concepts[bestconcept]).help_rating)
