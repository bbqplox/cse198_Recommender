class Concept(object):

    def __init__(self, n, pq, rq):
        self.name = n
        self.next_concept = None
        self.profile_qs = pq
        self.rec_qs = rq

    def setNextConcept(self, c):
        self.next_concept = c
