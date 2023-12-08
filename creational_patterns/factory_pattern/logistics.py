from abc import ABC, abstractmethod

# Creator class
class Logistics(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    def plan_delivery(self, cargo):
        # common logic for handling delivery
        transport = self.create_transport()
        transport.deliver(cargo)

# Concrete Creators
class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()

# Product interface
class Transport(ABC):
    @abstractmethod
    def deliver(self, cargo):
        pass

# Concrete Products
class Truck(Transport):
    def deliver(self, cargo):
        print(f"Delivering {cargo} by road in a truck")

class Ship(Transport):
    def deliver(self, cargo):
        print(f"Delivering {cargo} by sea in a ship")

# Client code
def logistics_client(logistics: Logistics, cargo):
    logistics.plan_delivery(cargo)

# Usage
road_logistics = RoadLogistics()
logistics_client(road_logistics, "Furniture")

sea_logistics = SeaLogistics()
logistics_client(sea_logistics, "Coal")
