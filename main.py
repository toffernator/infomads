from algorithms import IAlgorithm, EffectiveTicketPrice
from models import Instance, Day
from typing import Dict

import sys

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

def main():
    algorithms: Dict[str, IAlgorithm] = {
            "Effective ticket price": EffectiveTicketPrice()
            }
    
    instance = parse_input()
    schedule = algorithms["Effective ticket price"].run(instance)
    print(schedule.pretty_string())

if __name__ == "__main__":
    main()
