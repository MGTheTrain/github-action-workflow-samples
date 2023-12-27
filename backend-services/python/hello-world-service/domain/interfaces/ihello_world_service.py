from abc import ABC, abstractmethod

class IHelloWorldService(ABC):
    @abstractmethod
    def get_hello_world_message(self):
        pass