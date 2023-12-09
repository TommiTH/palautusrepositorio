from matchers import All, PlaysIn, HasAtLeast, HasFewerThan, And, Or


class QueryBuilder:
    def __init__(self, matchers = All()):
        self._matchers = matchers

    def build(self):
        return self._matchers

    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team), self._matchers))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value, attr), self._matchers))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value, attr), self._matchers))
    
    def oneOf(self, first, second):
        return QueryBuilder(Or(first, second))
