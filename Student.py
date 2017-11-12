class Student(object):

    def __init__(self, n, ct):
        self.name = n
        self.concept_table = ct #concept to one hot encoded profiling questions

    def updateConcept(self, cname, l):
        self.concept_table[cname] = l
