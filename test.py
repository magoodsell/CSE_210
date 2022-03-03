# the Employee interface
from typing_extensions import Self


class Employee:                    

    def calculate_pay(self):
        raise NotImplementedError("Method not implemented in interface.")


# a specific implementation of the Employee interface
class SalariedEmployee(Employee):

    def __init__(self):
        self._salary = 100
     
    def calculate_pay(self):
        return self._salary


# another implementation of the Employee interface
class HourlyEmployee(Employee):

    def __init__(self):
        self._rate = 9.0
        self._hours = 100

    def calculate_pay(self):
        return self._rate * self._hours




'''
# the Employee interface
class Employee:                    

    def calculate_pay(self):
        raise NotImplementedError("Method not implemented in interface.")


# a specific implementation of the Employee interface
class SalariedEmployee(Employee):

    def __init__(self):
        self._salary = 100
     
    def calculate_pay(self):
        return _salary


# another implementation of the Employee interface
class HourlyEmployee(Employee):

    def __init__(self):
        self._rate = 9.0
        self._hours = 100

    def calculate_pay(self):
        return _rate * _hours


'''
