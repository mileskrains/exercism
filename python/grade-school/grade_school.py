from collections import defaultdict


class School(object):
    def __init__(self, name):
        self.name = name
        self.roster = defaultdict(list)
        
    def add(self, student, grade):
        self.roster[grade].append(student)
    
    def grade(self, grade):
        students = self.roster[grade]
        return sorted(students)
    
    def sort(self):
        grades = sorted(self.roster.keys())
        return [(g, tuple(sorted(self.roster[g]))) for g in grades]
