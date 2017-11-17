class Garden(object):
    default_students = ('Alice Bob Charlie David Eve Fred '
                        'Ginny Harriet Ileana Joseph Kincaid Larry').split()
    plants_dict = dict(zip('GCRV', 'Grass Clover Radishes Violets'.split()))

    def __init__(self, diagram, students=None):
        self.diagram = diagram
        if students is None:
            self.students = self.default_students
        else:
            self.students = students
        self.diagram = diagram.split('\n')
        self.students.sort()
        self.student_numbers = {k: v for v, k in enumerate(self.students)}

    def plants(self, student):
        sn = self.student_numbers[student]
        sp = self.diagram[0][2*sn:2*sn+2] + self.diagram[1][2*sn:2*sn+2]
        return [self.plants_dict[k] for k in sp]
