class Question(object):

    def __init__(self, n, d, a):
        self.name = n
        self.description = d
        self.answer = a

class ProfileQuestion(Question):

    def __init__(self, n, d, a, l):
        Question.__init__(self, n, d, a)
        self.label = l

class RecQuestion(Question):

    def __init__(self, n, d, a, r):
        Question.__init__(self, n, d, a)
        self.help_rating = r
