from algorithms import IAlgorithm
from models import Instance, Schedule

class ExpectedPrice(IAlgorithm):
    def run(self, instance: Instance) -> Schedule:
        return Schedule(instance)

