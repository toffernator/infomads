from dataclasses import dataclass
from typing import List

@dataclass
class Entry:
    i: int
    s_i: int
    p_i: int
    h_i: int

@dataclass
class Instance:
    n: int
    m: int
    D: List[Entry] 

@dataclass
class Decision:
    flying: int
    staying: int

Schedule = List[Decision]
