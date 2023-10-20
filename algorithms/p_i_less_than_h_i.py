from algorithms import IAlgorithm
from models import Instance, Schedule


class BuyWheneverP_iLessThanH_i(IAlgorithm):
    def run(self, instance: Instance) -> Schedule:
        return Schedule(instance)
