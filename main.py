import sys

import numpy as np
import matplotlib.pyplot as plt

from algorithms import IAlgorithm, EffectiveTicketPrice, Greedy, BuyWheneverP_iLessThanH_i, ExpectedPrice
from models import Instance, instance_from
from typing import Dict, Generator, List

from pathlib import Path

OPT: str = "opt"
GREEDY: str = "greedy online"
BUY_WHENEVER_P_I_LESS_THAN_H_I: str = "Buy Whenver P_i < H_i with Cumalative Hotel Cost Constraint"
EXPECTED_PRICE: str = "expected price"

def main():
    # Configure
    algorithms: Dict[str, IAlgorithm] = {
        OPT: EffectiveTicketPrice(),
        GREEDY: Greedy(),
        BUY_WHENEVER_P_I_LESS_THAN_H_I: BuyWheneverP_iLessThanH_i(),
        EXPECTED_PRICE: ExpectedPrice()
    }
    examples: Path = Path(sys.argv[1])
    
    # Do stuff
    results: Dict[str, List[float]] = {
        OPT: [],
        GREEDY: [],
        BUY_WHENEVER_P_I_LESS_THAN_H_I: [],
        EXPECTED_PRICE: []
    }

    for instance in instances(examples):
       expected_price_cost = algorithms[EXPECTED_PRICE].run(instance).cost()
       expected_price_cost2 = algorithms[EXPECTED_PRICE].run(instance).cost()
       expected_price_cost3 = algorithms[EXPECTED_PRICE].run(instance).cost()
       print("first run call", expected_price_cost)
       print("second run call", expected_price_cost2)
       print("third run call", expected_price_cost3)
       for name, algorithm in algorithms.items():
           alg_cost = algorithm.run(instance).cost()
           results[name].append(alg_cost)

    averages: Dict[str, float] = {
        OPT: (sum(results[OPT]) / len(results[OPT])),
        GREEDY: (sum(results[GREEDY]) / len(results[GREEDY])),
        BUY_WHENEVER_P_I_LESS_THAN_H_I: (sum(results[BUY_WHENEVER_P_I_LESS_THAN_H_I]) / len(results[BUY_WHENEVER_P_I_LESS_THAN_H_I])),
        EXPECTED_PRICE: (sum(results[EXPECTED_PRICE]) / len(results[EXPECTED_PRICE])),
    }
    plt.bar(averages.keys(), averages.values())
    plt.axhline(y=1)
    # plt.show()


def instances(p: Path) -> Generator[Instance, None, None]:
    if p.is_dir():
        for input in p.glob("**/*.in"):
            yield instance_from(input)
    else:
        yield instance_from(p)


if __name__ == "__main__":
    main()
