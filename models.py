from dataclasses import dataclass, field
from typing import List
from pathlib import Path

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
    name: str

def instance_from(input: Path) -> Instance:
    with input.open("r") as f:
        n = int(f.readline())
        m = int(f.readline())

        days = []
        for i in range(m):
            line = f.readline()
            # This line is likely to fail if the input is malformed
            [s_i, p_i, h_i] = [int(x) for x in line.split(",")]
            days.append(Day(i, s_i, p_i, h_i))

        return Instance(n, m, days, input.name)

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
