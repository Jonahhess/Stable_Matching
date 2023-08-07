import queue
from person import Person, Gender

class Matching:
    matches: {Person:Person}

    def __init__(self,dating_pool) -> None:
        self.matches = {}
        self.do_stable_match(dating_pool)


    def do_stable_match(self, dating_pool) -> None:
        free_men_queue = queue.Queue()
        for i in dating_pool.get_men():
            free_men_queue.put(i)
        self.stable_matching(free_men_queue)

    def stable_matching(self,free_men_queue) -> None:
        while not free_men_queue.empty():
            suitor = free_men_queue.get()
            for i in suitor.pref_list[suitor.asked_out:]:
                suitor.asked_out = suitor.asked_out + 1
                cur = self.matches.get(i)
                if cur is None:
                    #print("new match! ")
                    self.pair_up(suitor, i)
                    break
                else:
                    if self.is_better_match(suitor, i, cur):
                        #print("switch! ")
                        self. unpair(cur, i)
                        self.pair_up(suitor, i)
                        free_men_queue.put(cur)
                        break

    def pair_up(self, man, woman) -> None:
        self.matches.update({man:woman})
        self.matches.update({woman:man})
        #print("Mr. ", man.id, " chose Ms. ", woman.id,
        #    "\nHis ", man.preference(woman), "choice. Her ",woman.preference(man), "choice.")

    def unpair(self, man, woman) -> None:
        self.matches.pop(man)
        self.matches.pop(woman)

    def is_better_match(self, man, woman, cur) -> bool:
        new = woman.pref_list.index(man)
        old = woman.pref_list.index(cur)
        loyal = woman.loyalty
        return new + loyal < old

    def average_rank(self) -> int:
        avg_rank = 0
        men_index = 0
        for k,_ in self.matches.items():
            if k.gender == Gender.MAN:
                men_index = men_index + 1
                avg_rank = avg_rank + k.asked_out

        if men_index < 1:
            men_index = 1
        avg_rank = avg_rank // men_index
        return avg_rank
