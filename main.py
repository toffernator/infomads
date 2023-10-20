from algorithms import IAlgorithm, EffectiveTicketPrice, Greedy
from models import Instance, Day
from typing import Dict

import sys

def main():
    algorithms: Dict[str, IAlgorithm] = {
        "OPT": EffectiveTicketPrice(),
        "Greedy online": Greedy(),
    }
    
    instance = parse_input()
    
    opt_schedule = algorithms["OPT"].run(instance)
    greedy_schedule = algorithms["Greedy online"].run(instance)
    
    print(opt_schedule.pretty_string())
    print("-------------------------------------------------------------------")
    print(greedy_schedule.pretty_string())

def parse_input() -> Instance:
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())

    days : list[Day] = []
    for i in range(m):
        line = sys.stdin.readline()
        # This line is likely to fail if the input is malformed
        [s_i, p_i, h_i] = [int(x) for x in line.split(",")]
        days.append(Day(i, s_i , p_i, h_i))

    return Instance(n, m, days)

if __name__ == "__main__":
    main()
