import sys

import matplotlib.pyplot as plt
import numpy as np

from algorithms import IAlgorithm, EffectiveTicketPrice, Greedy, BuyWheneverP_iLessThanH_i, ExpectedPrice
from models import Instance, instance_from
from typing import Dict, Generator, List

from pathlib import Path

OPT: str = "opt"
GREEDY: str = "greedy online"
BUY_WHENEVER_P_I_LESS_THAN_H_I: str = "buy whenever p_i < h_i with cumalative hotel cost constraint"
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
    results: Dict[str, List[float]] = {
        OPT: [],
        GREEDY: [],
        BUY_WHENEVER_P_I_LESS_THAN_H_I: [],
        EXPECTED_PRICE: []
    }
    for (i, instance) in enumerate(instances(examples)):
        opt_cost = algorithms[OPT].run(instance).cost()
        print("Instance #" + str(i), instance.name)
        for name, algorithm in algorithms.items():
            alg_cost = algorithm.run(instance).cost()
            instance_ratio =  round(alg_cost / opt_cost, 3)
            results[name].append(instance_ratio)
            print("{}: {} ({})".format(name, alg_cost, instance_ratio))

    averages: Dict[str, float] = {
        OPT: (sum(results[OPT]) / len(results[OPT])),
        GREEDY: (sum(results[GREEDY]) / len(results[GREEDY])),
        BUY_WHENEVER_P_I_LESS_THAN_H_I: (sum(results[BUY_WHENEVER_P_I_LESS_THAN_H_I]) / len(results[BUY_WHENEVER_P_I_LESS_THAN_H_I])),
        EXPECTED_PRICE: (sum(results[EXPECTED_PRICE]) / len(results[EXPECTED_PRICE])),
    }

    viridis_map = plt.get_cmap("viridis")
    colors = [viridis_map(i) for i in np.linspace(0, 1, len(averages))]

    plt.title("Average Competitive Ratio for the Different Algorithms Across 9320 Randomly Generated Feasible Instances", fontsize=18)
    plt.ylabel("Average Competitive Ratio", fontsize=16)
    plt.xlabel("Algorithm", fontsize=16)
    plt.bar([name.title() for name in averages.keys()], averages.values(), color=colors)

    # Add the values to the y-axis
    for i, average in enumerate(averages.values()):
        plt.text([name.title() for name in averages.keys()][i], average + 0.05, str(average), ha='center', va='bottom', fontsize=14)

    plt.show()

def instances(p: Path) -> Generator[Instance, None, None]:
    if p.is_dir():
        for input in p.glob("**/*.in"):
            yield instance_from(input)
    else:
        yield instance_from(p)

if __name__ == "__main__":
    main()
