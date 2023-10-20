from abc import ABC, abstractmethod
from models import Instance, Schedule

class IAlgorithm(ABC):
    @abstractmethod
    def run(self, instance: Instance) -> Schedule:
        pass

