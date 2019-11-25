# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    """Base vehicle class"""
    def __init__(self):
        pass

class FlightVehicle(Vehicle):
    """Vehicles that can fly"""
    def __init__(self):
        pass

class GroundVehicle(Vehicle):
    """Vehicles that drive on the ground"""
    def __init__(self):
        pass

class Starship(FlightVehicle):
    def __init__(self):
        pass

class Airplane(FlightVehicle):
    def __init__(self):
        pass

class Car(GroundVehicle):
    def __init__(self):
        pass

class Motorcycle(GroundVehicle):
    def __init__(self):
        pass