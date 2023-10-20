from algorithms import IAlgorithm
from models import Decision, Instance, Schedule

class Greedy(IAlgorithm):
    def run(self, instance: Instance) -> Schedule:
        num_people_remaining: int = instance.n
        flying = [0] * instance.m
        for i, day in enumerate(instance.days):
            flying[i] = min(day.s_i, num_people_remaining)
            num_people_remaining -= flying[i]

        schedule: Schedule = Schedule(instance)
        num_people_remaining = instance.n
        for flys_today in flying:
            num_people_remaining -= flys_today
            schedule.decisions.append(Decision(flys_today, num_people_remaining))
        
        return schedule
