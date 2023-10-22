from algorithms import IAlgorithm
from models import Decision, Instance, Schedule



class BuyWheneverP_iLessThanH_i(IAlgorithm):
    def run(self, instance: Instance) -> Schedule:
        num_people_remaining: int = instance.n
        flying = [0] * instance.m
        cumulative = 0
        for i, day in enumerate(instance.days):
            if cumulative > day.p_i or day.p_i < day.h_i :
                flying[i] = min(day.s_i, num_people_remaining)
                num_people_remaining -= flying[i]

            cumulative += day.h_i

        
        schedule: Schedule = Schedule(instance)
        num_people_remaining = instance.n
        for flys_today in flying:
            num_people_remaining -= flys_today
            schedule.decisions.append(Decision(flys_today, num_people_remaining))
        
        return schedule
    
