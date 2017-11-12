from Student import *
from Concept import *
from Question import *

def createDummyConcept(name):
    profilingQs = []
    recQs = []
    for i in range(5):
        profilingQs.append(ProfileQuestion("q" + str(i+1), "the question", "the answer", i))
        recQs.append(RecQuestion("q" + str(i+1), "the question", "the answer", i*0.75))

    c = Concept(name, profilingQs, recQs)

    return c

concepts = []
concepts.append(createDummyConcept("c1"))
concepts.append(createDummyConcept("c2"))
concepts.append(createDummyConcept("c3"))
concepts.append(createDummyConcept("c4"))
concepts[0].setNextConcept(concepts[1])
concepts[1].setNextConcept(concepts[2])
concepts[3].setNextConcept(concepts[2])

ctable = {}
for c in concepts:
    ctable[c.name] = [0]*len(c.profile_qs)

s1 = Student("s1", ctable)
s2 = Student("s2", ctable)
