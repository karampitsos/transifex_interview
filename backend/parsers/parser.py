from abc import ABC, abstractmethod
from typing import Dict


class Parser(ABC):
    
    @abstractmethod
    def parse(self, data: Dict) -> str:
        pass