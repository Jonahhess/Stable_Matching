import random

def create_preferences(n_men, n_women):
    msw = [i for i in range(n_men)]
    for i in msw:
        pref_list = [j for j in range(n_men, n_men+n_women)]
        random.shuffle(pref_list)
        msw[i] = tuple(pref_list)
    
    wsm = [i for i in range(n_men, n_men+n_women)]
    for i in range(len(wsm)):
        pref_list = [j for j in range(n_men)]
        random.shuffle(pref_list)
        wsm[i] = tuple(pref_list)
    return msw,wsm

def stable_matching(msw, wsm, loyalty):
    matches = {}
    
    for i in range(len(msw)):
        for j in range(len(wsm)):
            current_woman = msw[i][j]
            cw_index = current_woman - len(msw)
            candidate_rank = wsm[cw_index].index(i)
            if current_woman not in matches.values():
                matches[i] = current_woman
                matches[current_woman] = i
                print("new match: ", i, " chose", current_woman, 
                      " \nHis ", j, " choice. Her ", candidate_rank, " choice.")
                break
            else:
                her_current_match = matches[current_woman]
                if candidate_rank > her_current_match + loyalty:
                    matches[current_woman] = None
                    matches[j] = current_woman
                    print("switch: ", j, " chose", current_woman, 
                      " \nHis ", i, " choice. Her ", candidate_rank, " choice.")

    print(matches)

'''
    Initialize all m ∈ M and w ∈ W to free
    while ∃ free man m who still has a woman w to propose to {
       w = first woman on m’s list to whom m has not yet proposed
       if w is free
         (m, w) become engaged
       else some pair (m', w) already exists
         if w prefers m to m'
            m' becomes free
           (m, w) become engaged 
         else
           (m', w) remain engaged
''' 

def main():
    msw,wsm = create_preferences(5,5)
    print(msw)
    print(wsm)
    
    stable_matching(msw,wsm,0)

main()