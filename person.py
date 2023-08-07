from enum import Enum

Gender = Enum('gender', ['MAN', 'WOMAN'])

class Person:
    id:int
    gender:Gender
    loyalty:int
    pref_list:list
    asked_out:int

    def __init__(self, id, gender, loyalty, pref_list=None,asked_out=0):
        self.id = id
        self.gender = gender
        self.loyalty = loyalty
        self.pref_list = pref_list
        self.asked_out = asked_out