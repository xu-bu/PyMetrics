import abc
import inspect

from Rental import Rental

class Customer(metaclass=abc.ABCMeta):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.rental=[]

    def addRental(self,rental:Rental):
        self.rental.append(rental)

    @abc.abstractmethod
    def read(self):
        pass