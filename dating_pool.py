import random
from person import Person, Gender

class Dating_Pool:
    men:list[Person]
    women:list[Person]

    def __init__(self,n_men,n_women,loyalty) -> None:
        self.men,self.women = self.create_men_and_women(n_men,n_women,loyalty)
        self.generate_preferences()

    def create_men_and_women(self, n_men, n_women, loyalty):
        men = []
        women = []
        for i in range(n_men):
            man = Person(i, Gender.MAN, loyalty)
            men.append(man)
        for i in range(n_women):
            woman = Person(i, Gender.WOMAN, loyalty)
            women.append(woman)
        return men, women

    def generate_pref_list(self, person, people) -> None:
        pref_list = [i for i in people]
        random.shuffle(pref_list)
        person.pref_list = pref_list

    def generate_preferences(self) -> None:
        for i in self.men:
            self.generate_pref_list(i, self.women)
        for i in self.women:
            self.generate_pref_list(i, self.men)

    def get_men(self):
        return self.men