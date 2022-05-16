from abc import ABC, abstractmethod

class Resource(ABC):

    @abstractmethod
    def list_by_name(self):
        pass

    @abstractmethod
    def delete(self, resource_name):
        pass