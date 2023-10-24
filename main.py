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
    
    # Do Stuff
    instances: Generator[Instance, None, None] = (
            instance_from(input) for input in examples.glob("**/*.in")
    )
    
    results: Dict[str, List[float]] = {
        OPT: [],
        GREEDY: [],
        BUY_WHENEVER_P_I_LESS_THAN_H_I: [],
        EXPECTED_PRICE: []
    }
    for instance in instances:
        opt_cost = algorithms[OPT].run(instance).cost()
        for name, algorithm in algorithms.items():
            alg_cost = algorithm.run(instance).cost()
            instance_ratio =  alg_cost / opt_cost
            results[name].append(instance_ratio)
    
    averages: Dict[str, float] = {
        OPT: (sum(results[OPT]) / len(results[OPT])),
        GREEDY: (sum(results[GREEDY]) / len(results[GREEDY])),
        BUY_WHENEVER_P_I_LESS_THAN_H_I: (sum(results[BUY_WHENEVER_P_I_LESS_THAN_H_I]) / len(results[BUY_WHENEVER_P_I_LESS_THAN_H_I])),
        EXPECTED_PRICE: (sum(results[EXPECTED_PRICE]) / len(results[EXPECTED_PRICE])),
    }
    plt.bar(averages.keys(), averages.values())
    plt.show()


if __name__ == "__main__":
    main()
