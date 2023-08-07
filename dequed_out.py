import random
from collections import deque
from enum import Enum

Gender = Enum('gender', ['MAN', 'WOMAN'])

class Person:
    id:int
    gender:Gender
    loyalty:int
    pref_deque:deque
    deque_capacity:int
    deque_size:int

    def __init__(self, id, gender, loyalty, pref_deque=None,deque_size=0):
        self.id = id
        self.gender = gender
        self.loyalty = loyalty
        self.pref_deque = pref_deque
        self.deque_size = deque_size
    
    def __hash__(self):
        return hash((self.id, self.gender))

    def preference(self, candidate):
        return self.pref_deque.index(candidate)


def create_men_and_women(n_men, n_women, loyalty):
    men = []
    women = []
    for i in range(n_men):
        man = Person(i, Gender.MAN, loyalty)
        men.append(man)
    for i in range(n_women):
        woman = Person(i, Gender.WOMAN, loyalty)
        women.append(woman)
    return men, women

def generate_pref_deque(person, people):
    pref_list = [i for i in people]
    random.shuffle(pref_list)
    pref_deque = deque()
    deque_size = 0
    for i in pref_list:
        pref_deque.append(i)
        deque_size = deque_size + 1
    person.pref_deque = pref_deque
    person.deque_capacity = deque_size
    person.deque_size = deque_size

def generate_preferences(men, women):
    for i in men:
        generate_pref_deque(i, women)
    for i in women:
        generate_pref_deque(i, men)

def unpair(matches, man, woman):
    matches.pop(man)
    matches.pop(woman)

    return matches

def pair_up(matches, man, woman):
    matches.update({man:woman})
    matches.update({woman:man})
    #print("Mr. ", man.id, " chose Ms. ", woman.id,
    #    "\nHis ",man.deque_capacity-man.deque_size-1 , "choice. Her ",woman.preference(man), "choice.")
    return matches

def is_better_match(man, woman, cur):
    new = woman.pref_deque.index(man)
    old = woman.pref_deque.index(cur)
    loyal = woman.loyalty
    return new + loyal < old

def stable_matching(free_men_deque):
    matches = {}
    while free_men_deque:
        suitor = free_men_deque.popleft()
        while suitor.pref_deque:
            i = suitor.pref_deque.popleft()
            suitor.deque_size = suitor.deque_size-1
            cur = matches.get(i)
            if cur is None:
                #print("new match! ")
                matches = pair_up(matches, suitor, i)
                break
            else:
                if is_better_match(suitor, i, cur):
                    #print("switch! ")
                    matches = unpair(matches, cur, i)
                    matches = pair_up(matches, suitor, i)
                    free_men_deque.appendleft(cur)
                    break
    return matches

def average_rank(matching, gender):
    rank = 0
    n_gender = 0
    for k,v in matching.items():
        if k.gender == gender:
            rank = rank + k.deque_size
            n_gender = n_gender + 1
    return rank // n_gender
    

def do_stable_match(n_men,n_women,loyalty):
    men, women = create_men_and_women(n_men, n_women,loyalty)
    generate_preferences(men, women)

    free_men_deque = deque()
    for i in men:
        free_men_deque.append(i)

    matching = stable_matching(free_men_deque)
    avg_rank = average_rank(matching, Gender.MAN)
    return avg_rank

def main():
    n_women = 40
    tries = 30
    for i in range(n_women-10,n_women+10): # men
        for j in range(10): # loyalty
            avg_rank = 0
            for k in range(tries): # 10 tries
                avg_rank = avg_rank + do_stable_match(i,n_women,j)
            avg_rank = avg_rank // tries
            print(j,i,n_women,avg_rank)

if __name__ == '__main__':
    main()