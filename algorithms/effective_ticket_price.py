from dataclasses import dataclass
import sys

@dataclass
class Entry:
  day: int; seats: int; price: int; hotel: int; cost: int

def read_input() -> tuple[int, int, list[Entry]]:
  n = int(sys.stdin.readline())
  m = int(sys.stdin.readline())

  entries : list[Entry] = []
  acc_hotel_cost = 0

  for i in range(m):
    line = sys.stdin.readline()
    [s, p, h] = [int(x) for x in line.split(",")]
    cost = p + acc_hotel_cost
    entries.append(Entry(i, s, p, h, cost))
    acc_hotel_cost += h

  return (n, m, entries)

Schedule = tuple[int, int] # flying, staying

def generate_schedule(n: int, m: int, entries: list[Entry]) -> list[Schedule]:
  sorted_entries = sorted(entries, key=lambda e: e.cost) # sort by effective cost (last entry)
  flying = [0] * m
  num_people = n
  for entry in sorted_entries:
    tickets = min(entry.seats, num_people)
    flying[entry.day] = tickets
    num_people -= tickets
    if num_people == 0: break

  num_people = n
  schedules : list[Schedule] = []
  for f in flying:
    num_people -= f
    schedules.append((f, num_people))
    if num_people == 0: break

  return schedules

def calc_schedule_cost (schedules: list[Schedule], entries: list[Entry]) -> int :
  return sum([
      flying * e.price + staying * e.hotel
      for ((flying, staying), e) in zip(schedules, entries)
    ])

(n, m, entries) = read_input()
sched = generate_schedule(n, m, entries)

for (f, s) in sched:
  print(str(f) + ", " + str(s))

print(calc_schedule_cost(sched, entries))
