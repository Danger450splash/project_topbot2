from abc import ABC, abstractmethod

# Abstract Class
class AbstractClass(ABC):

    @abstractmethod
    def market_menu(self) -> None:
        pass

    @abstractmethod
    def AuthenticateATM(self) -> None:
        pass

    @abstractmethod
    def ATM(self) -> None:
        pass