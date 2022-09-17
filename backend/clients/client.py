from abc import ABC, abstractmethod
from typing import Dict


class Client(ABC):

    @abstractmethod
    async def get(self, **kwargs) -> Dict:
        pass
