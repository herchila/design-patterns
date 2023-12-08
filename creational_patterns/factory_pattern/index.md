The Factory Pattern is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. A practical use case for the Factory Pattern is in the development of a logistics management application, where different types of transportation vehicles are needed.

In a logistics application, you may need to handle various types of transportation like trucks, ships, and airplanes. Each transportation type has its own way of processing cargo. Using the Factory Pattern, you can define a common interface for creating these transportation objects and delegate the instantiation to subclasses that handle the specific creation logic for each type of vehicle.

Take a look [this implementation](./logistics.py):

* `Logistics` is an abstract class (or Creator) with an abstract method `create_transport` and a method `plan_delivery` which contains common logic for planning a delivery.
* `RoadLogistics` and SeaLogistics are concrete creators that override the `create_transport` method to return a specific type of transport (Truck or Ship).
* `Transport` is an abstract product class with an abstract method `deliver`.
* `Truck` and `Ship` are concrete products implementing the `Transport` interface with specific delivery methods.
* The client code (`logistics_client`) demonstrates how the factory pattern can be used to handle deliveries without knowing the details of how each type of transport works.

This design allows the logistics application to easily introduce new types of transportation without changing the existing code, adhering to the Open/Closed Principle. It provides a flexible and scalable way to manage different transportation methods in a logistics system.
