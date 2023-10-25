from .algorithm import IAlgorithm
from models import Day, Decision, Instance, Schedule
from typing import List

class EffectiveTicketPrice(IAlgorithm):
    def run(self, instance: Instance) -> Schedule:
        effective_ticket_prices = self._compute_effective_ticket_prices(instance.m, instance.days)
        sorted_effective_ticket_prices = sorted(effective_ticket_prices, key=lambda day: day.p_i)

        flying = [0] * instance.m
        num_people_remaining = instance.n
        for day in sorted_effective_ticket_prices:
            tickets = min(day.s_i, num_people_remaining)
            flying[day.i] = tickets
            num_people_remaining -= tickets
            if num_people_remaining == 0: break
 
        schedule: Schedule = Schedule(instance)
        num_people_remaining = instance.n
        for flys_today in flying:
            num_people_remaining -= flys_today
            schedule.decisions.append(Decision(flys_today, num_people_remaining))
            if num_people_remaining == 0: break

        return schedule

    def _compute_effective_ticket_prices(self, m: int, days: List[Day]) -> List[Day]:
        # Copy to avoid mutating the original instance
        effective_ticket_prices: List[Day] = days.copy()
        
        accumlative_hotel_cost: int = 0
        for i in range(m):
            effective_price = days[i].p_i + accumlative_hotel_cost
            accumlative_hotel_cost += days[i].h_i

            effective_ticket_prices[i].p_i = effective_price
        
        return effective_ticket_prices

