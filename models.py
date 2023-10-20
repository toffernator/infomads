from dataclasses import dataclass, field
from typing import List

@dataclass
class Day:
    i: int
    s_i: int
    p_i: int
    h_i: int

@dataclass
class Instance:
    n: int
    m: int
    days: List[Day] 

@dataclass
class Decision:
    flying: int
    staying: int

@dataclass
class Schedule:
    instance: Instance
    decisions: List[Decision] = field(default_factory=list)

    def cost(self):
        return sum([
            decision.flying * day.p_i + decision.staying * day.h_i
            for (decision, day) in zip(self.decisions, self.instance.days)
        ])
    
    def pretty_string(self) -> str:
        pretty_string = f"{'day':<4} | {'flying':<10} | {'staying':<10} |\n"
        for i, decision in enumerate(self.decisions):
            pretty_string += f"{i:<4} | {decision.flying:<10} | {decision.staying:<10} |\n"
        pretty_string += f"Cost: {self.cost()}"
        return pretty_string.strip()
