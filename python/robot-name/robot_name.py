import random
import string
import time

class Robot(object):
    robot_pop = []
    
    @staticmethod
    def make_name():
        random.seed(time.time())
        alpha_part = random.choices(string.ascii_uppercase, k=2)
        num_part = random.choices(string.digits, k=3)
        return ''.join(alpha_part + num_part)
    
    @classmethod
    def register_unique_name(cls):
        name = cls.make_name()
        while name in cls.robot_pop:
            name = cls.make_name()
        cls.robot_pop.append(name)
        return name
    
    @classmethod
    def remove_name(cls, name):
        cls.robot_pop.remove(name)
        
    def __init__(self):
        self.assign_name()
    
    def assign_name(self):
        name = self.register_unique_name()
        self.name = name
        
    def reset(self):
        self.remove_name(self.name)
        self.assign_name()
        