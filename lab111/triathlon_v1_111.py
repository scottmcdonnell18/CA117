class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.discipline = {}

    def __str__(self):
        l = []
        l.append('Name: {}'.format(self.name))
        l.append('ID: {}'.format(self.tid))
        l.append('Race time: {}'.format(sum(self.discipline.values())))
        return '\n'.join(l)

    def add_time(self, sport, time):
        self.discipline[sport] = time

    def get_time(self, sport):
        return self.discipline[sport]

    def total_time(self):
        return sum(self.discipline.values())

    def __eq__(self, other):
        return self.total_time() == other.total_time()

    def __gt__(self, other):
        return self.total_time() > other.total_time()

    def __lt__(self, other):
        return self.total_time() < other.total_time()

class Triathlon(Triathlete):

    def __init__(self):
        self.d = {}

    def add(self, t1):
        self.d[t1.tid] = t1

    def remove(self, t1):
        del self.d[t1]

    def lookup(self, t1):
        try:
            return self.d[t1]
        except:
            return None
