from algorithms import IAlgorithm, EffectiveTicketPrice
from models import Instance, Schedule, Decision
import copy

class ExpectedPrice(IAlgorithm):
    def run(self, instance: Instance) -> Schedule:

        expectedDays: List[instance.m] = copy.deepcopy(instance.days)
        schedule: Schedule = Schedule(instance)
        n = instance.n

        for i in range(instance.m):
            #start with the first day as "average"
            expectedDays[i].p_i = expectedDays[0].p_i
            expectedDays[i].h_i = expectedDays[0].h_i
            expectedDays[i].s_i = expectedDays[0].s_i

        for i in range(instance.m-1):
            expectedDays = self._update_avg(expectedDays, instance, i)

            s = EffectiveTicketPrice().run(Instance(instance.n, instance.m, expectedDays, ""))
            schedule.decisions.append(s.decisions[0])

            n -= s.decisions[0].flying
            if n == 0: break

        if n != 0:
            schedule.decisions.append(Decision(n, 0))

        return schedule

    def _update_avg(self, exp_days, inst, d):
        cur_avg = exp_days[d-1]

        new_avg_p_i = (cur_avg.p_i*d + inst.days[d].p_i) / (d+1)
        new_avg_h_i = (cur_avg.h_i*d + inst.days[d].h_i) / (d+1)
        new_avg_s_i = (cur_avg.s_i*d + inst.days[d].s_i) / (d+1)

        for i, day in enumerate(inst.days[d:], start = d):
            exp_days[i].p_i = round(new_avg_p_i)
            exp_days[i].h_i = round(new_avg_h_i)
            exp_days[i].s_i = round(new_avg_s_i)
        return exp_days
