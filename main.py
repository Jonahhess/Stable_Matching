from person import Gender
from dating_pool import Dating_Pool
from matching import Matching

def main():
    n_women = 40
    runs = 30
    print("loyalty,n_men,n_women,avg_rank")
    for n_men in range(n_women-10,n_women+10):
        for loyalty in range(10):
            dating_pool = Dating_Pool(n_men,n_women,loyalty)
            matching = Matching(dating_pool)
            avg_rank = 0
            for _ in range(runs):
                avg_rank = avg_rank + matching.average_rank()
            avg_rank = avg_rank // runs
            print(loyalty,n_men,n_women,avg_rank)


if __name__ == '__main__':
    main()