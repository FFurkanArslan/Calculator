from abc import ABCMeta, abstractmethod

class CalculateBase(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def add(self,a,b):
        pass
    
    @abstractmethod
    def substract(self,a,b):
        pass
    @abstractmethod
    def multiply(self,a,b):
        pass
    @abstractmethod
    def divide(self,a,b):
        pass
    @abstractmethod
    def mod(self,a,b):
        pass
    
    @abstractmethod
    def logarithm(self,a):
        pass
    
        
    