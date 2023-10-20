from algorithms import IAlgorithm, EffectiveTicketPrice, Greedy, BuyWheneverP_iLessThanH_i, ExpectedPrice
from models import Instance, Day
from typing import Dict

import sys

def main():
    # Configure
    algorithms: Dict[str, IAlgorithm] = {
        "OPT": EffectiveTicketPrice(),
        "Greedy online": Greedy(),
        "Buy Whenver P_i < H_i with Cumalative Hotel Cost Constraint": BuyWheneverP_iLessThanH_i(),
        "Expected Price": ExpectedPrice()
    }
    
    # Do Stuff
    instance = parse_input()

    for name, algorithm in algorithms.items():
        print("".join(["-"] * 80))
        print(name)
        
        schedule = algorithm.run(instance)
        print(schedule.pretty_string())
    print("".join(["-"] * 80))

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
