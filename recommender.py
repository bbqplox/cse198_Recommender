from Student import *
from Concept import *
from ConceptGraph import *
from Question import *
import numpy as np

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
