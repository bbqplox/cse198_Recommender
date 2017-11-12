class Concept(object):

    def __init__(self, n, pq, rq):
        self.name = n
        self.next_concepts = []
        self.prev_concepts = []
        self.profile_qs = pq
        self.rec_qs = rq

    def connectConcept(self, c):
        self.next_concepts.append(c)
        c.prev_concepts.append(self)
