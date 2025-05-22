from abc import ABC, abstractmethod
from typing import Dict, Any

class StoreObject(ABC):

    @abstractmethod
    def get_key(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

class StoreHandler:
    store_map: Dict[str, Any]

    def __init__(self):
        self.store_map = {}

    def set_data(self, store_obj: StoreObject):
        self.store_map[store_obj.get_key()] = store_obj.get_data()

    def get_data(self, key: str) -> Any:
        return self.store_map.get(key)
