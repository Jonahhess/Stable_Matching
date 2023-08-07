import random
import queue
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
    
    def __hash__(self):
        return hash((self.id, self.gender))

    def preference(self, candidate):
        return self.pref_list.index(candidate)


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

def generate_pref_list(person, people):
    pref_list = [i for i in people]
    random.shuffle(pref_list)
    person.pref_list = pref_list

def generate_preferences(men, women):
    for i in men:
        generate_pref_list(i, women)
    for i in women:
        generate_pref_list(i, men)

def unpair(matches, man, woman):
    matches.pop(man)
    matches.pop(woman)

    return matches

def pair_up(matches, man, woman):
    matches.update({man:woman})
    matches.update({woman:man})
    #print("Mr. ", man.id, " chose Ms. ", woman.id,
    #    "\nHis ", man.preference(woman), "choice. Her ",woman.preference(man), "choice.")
    return matches

def is_better_match(man, woman, cur):
    new = woman.pref_list.index(man)
    old = woman.pref_list.index(cur)
    loyal = woman.loyalty
    return new + loyal < old

def stable_matching(free_men_queue):
    matches = {}
    while not free_men_queue.empty():
        suitor = free_men_queue.get()
        for i in suitor.pref_list[suitor.asked_out:]:
            suitor.asked_out = suitor.asked_out + 1
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
                    free_men_queue.put(cur)
                    break
    return matches

def average_rank(matching, gender):
    avg_rank = 0
    men_index = 0
    for k,_ in matching.items():
        if k.gender == Gender.MAN:
            men_index = men_index + 1
            avg_rank = avg_rank + k.asked_out

    if men_index < 1:
        men_index = 1
    avg_rank = avg_rank // men_index
    return avg_rank

def do_stable_match(n_men,n_women,loyalty):
    men, women = create_men_and_women(n_men, n_women,loyalty)
    generate_preferences(men, women)

    free_men_queue = queue.Queue()
    for i in men:
        free_men_queue.put(i)

    matching = stable_matching(free_men_queue)
    result = average_rank(matching, Gender.MAN)
    return result

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