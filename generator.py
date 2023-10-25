from dataclasses import dataclass
from pathlib import Path
from random import randrange, seed

# This will avoid integer overflow errors when summing all the costs to get an average
LOWER_PRICE = 1
UPPER_PRICE = 10000


@dataclass
class Instance:
    n: int
    m: int
    s: list[int]
    p: list[int]
    h: list[int]

    def save(self, file_name: str):
        dir = Path("instances")
        dir.mkdir(exist_ok=True)
        input = dir / Path(file_name)
        input.write_text(self.__str__())


    def __str__(self) -> str:
        txt_output = f"{self.n}\n{self.m}"
        for i in range(self.m):
            txt_output = txt_output + f"\n{self.s[i]}, {self.p[i]}, {self.h[i]}"
        return txt_output.strip()

@dataclass
class Decision:
    flights: int
    hotels: int

@dataclass
class Solution:
    instance: Instance
    ds: list[Decision]
    
    def flights_purchased(self) -> int:
        return sum(list(map(lambda d: d.flights, self.ds)))

    def flights_remaining(self) -> int:
        return self.instance.n - self.flights_purchased()

    def is_valid_solution(self) -> bool:
        return self.flights_remaining() == 0
    
    def cost(self) -> int:
        cost = 0
        for i in range(len(self.ds)):
            cost = cost + (self.ds[i].flights * self.instance.p[i]) + (self.ds[i].hotels * self.instance.h[i])
        return cost

    def save_to(self, dir):
        dir = Path(dir)
        dir.mkdir(exist_ok=True)

        input = dir / "input.txt"
        output = dir / "output.txt"

        input.write_text(self.instance.__str__())
        output.write_text(self.__str__())
    
    def __len__(self):
        return len(self.ds)
    
    def __str__(self):
        res = ""
        for d in self.ds:
            res = res + f"\n{d.flights}, {d.hotels}"
        return res.strip()

def create_instance(n, m) -> Instance:
    # n is the number of colleagues that needs to be sent home, and m is the
    # number of days within which they must be sent home.
    s = []
    p = []
    h = []
    
    for day in range(m-1):
        s.append(randrange(1, n))
        p.append(randrange(LOWER_PRICE, UPPER_PRICE))
        h.append(randrange(LOWER_PRICE, UPPER_PRICE))
    
    if sum(s) < n:
        s.append(n - sum(s))
        p.append(randrange(LOWER_PRICE, UPPER_PRICE))
        h.append(randrange(LOWER_PRICE, UPPER_PRICE))
    else:
        s.append(randrange(1, n))
        p.append(randrange(LOWER_PRICE, UPPER_PRICE))
        h.append(randrange(LOWER_PRICE, UPPER_PRICE))


    return Instance(n, m, s, p, h)

seed(1)
counter = 1;
for n in range(2, 51):
    for m in range(2, 21):
        for i in range(10):
            instance = create_instance(n, m)
            instance.save(f"n-{n}-m-{m}-{i}.in")
