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
